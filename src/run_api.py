from flask import Flask, request, jsonify
import Log as log

logger = log.setup_logger()

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


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
    return jsonify({"message": msg})

@app.route("/call_elevator/floor/<int:floor_number>")
def floor_action(floor_number: int):

    msg = f"Elevator Requested from FLOOR {floor_number}"
    logger.info(msg)
    return jsonify({"message": msg})

if __name__ == "__main__":
    app.run(debug=True)
