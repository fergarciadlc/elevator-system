from Motor import MotorState
from Dispatcher import ElevatorDispatcher
from Floor import FloorSystem
from Elevator import ElevatorSystem
import Log as log

logger = log.setup_logger()

def main():
    logger.info("hola mundo")
    elevator_1 = ElevatorSystem(idx=1, number_of_floors=5)
    logger.info(elevator_1)

def run():
    logger.info("otra")

def test_run():
    """Main run function, demostrative behavior"""
    NUMBER_OF_FLOORS = 7

    """Initializing elevators, floors and dispatcher"""
    dispatcher = ElevatorDispatcher()  # dispatcher

    # Initializing elevatos with id
    elevator_1 = ElevatorSystem(idx=1, number_of_floors=NUMBER_OF_FLOORS)
    elevator_2 = ElevatorSystem(idx=2, number_of_floors=NUMBER_OF_FLOORS)

    # Initializing floors
    floors = FloorSystem.generate_floors(NUMBER_OF_FLOORS)

    """Functionality"""
    # presseing a button from inside elevator
    elevator_1.press_elevator_button(3)

    # calling elevator 2 from floor 2
    floors[2].call_elevator_from_floor(elevator_2)

    # Requesting the nearest elevator from floor 6
    requested_floor = 6
    floors[requested_floor].call_elevator_from_floor(
        dispatcher.request_elevator_from_floor(
            requested_floor, [elevator_1, elevator_2]
        )
    )

    """Sepecial cases:"""
    # open door elevator 1
    elevator_1.door.open_door()
    # elevator_1.move_one_floor(MotorState.DOWN) # error, Exception: Elevator cannot go DOWN, Door is: Open.
    elevator_1.door.close_door()
    elevator_1.move_one_floor(MotorState.DOWN)
    logger.info(elevator_1)

if __name__ == "__main__":
    # main()
    # run()
    test_run()