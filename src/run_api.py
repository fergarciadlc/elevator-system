from Dispatcher import ElevatorDispatcher
from Floor import FloorSystem
from Elevator import ElevatorSystem
from flask import Flask, request, jsonify
import Log as log

logger = log.setup_logger()

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

NUMBER_OF_FLOORS = 7
dispatcher = ElevatorDispatcher()  # dispatcher

# Initializing floors
floors = FloorSystem.generate_floors(NUMBER_OF_FLOORS)

elevators = {
    1: ElevatorSystem(idx=1, number_of_floors=NUMBER_OF_FLOORS),
    2: ElevatorSystem(idx=2, number_of_floors=NUMBER_OF_FLOORS),
}


def get_type(value):
    """Returns a dict with the type of its values,

    Example:
    d = {"id":1, "message": "test", "value": 3.1416}
    get_type(d)
    >> {'id': "<class 'int'>", 'message': "<class 'str'>", 'value': "<class 'float'>"}
    """
    if isinstance(value, dict):
        return {key: get_type(value[key]) for key in value}
    else:
        return str(type(value))


@app.route("/elevator/", methods=["POST"])
def elevator_action():
    required_struct = {"elevator_id": int(), "button_press": int()}
    request_data = request.json
    if get_type(request_data) != get_type(required_struct):
        return (
            jsonify(
                {
                    "message": f"invalid json struct",
                    "required_struct": get_type(required_struct),
                }
            ),
            400,
        )
    elevator_id = request_data["elevator_id"]
    button_press = request_data["button_press"]
    msg = f"Elevator {elevator_id} - button pressed: {button_press}"
    logger.info(msg)
    elevators[elevator_id].press_elevator_button(button_press)
    return jsonify({"message": msg})


@app.route("/call_elevator/floor/<int:floor_number>")
def floor_action(floor_number: int):

    msg = f"Elevator Requested from FLOOR {floor_number}"
    logger.info(msg)

    requested_floor = floor_number
    floors[requested_floor].call_elevator_from_floor(
        dispatcher.request_elevator_from_floor(
            requested_floor, [e for e in elevators.values()]
        )
    )

    return jsonify({"message": msg})


@app.route("/check/")
def check_elevators():
    logger.info("Check state of elevators from API")

    def elevator_api_parser(elevator: ElevatorSystem) -> dict:
        return {
            "elevator_id": elevator.idx,
            "current_floor": elevator.current_floor,
            "motor_state": str(elevator.motor),
            "door": str(elevator.door),
        }

    d_out = {}
    for e_key in elevators.keys():
        logger.info(f"ELEVATOR: {elevators[e_key]}")
        d_out[e_key] = elevator_api_parser(elevators[e_key])

    return jsonify(d_out)


if __name__ == "__main__":
    app.run(debug=True)
