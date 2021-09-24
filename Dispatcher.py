from Floor import FloorSystem
from Elevator import ElevatorSystem


class ElevatorDispatcher:
    pass


if __name__ == "__main__":
    NUMBER_OF_FLOORS = 7

    e1 = ElevatorSystem(idx=1, number_of_floors=NUMBER_OF_FLOORS)
    e1.press_elevator_button(3)

    e2 = ElevatorSystem(idx=2, number_of_floors=NUMBER_OF_FLOORS)

    floors = FloorSystem.generate_floors(NUMBER_OF_FLOORS)

    floors[2].call_elevator_from_floor(e2)
