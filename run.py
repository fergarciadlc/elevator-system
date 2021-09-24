from Floor import FloorSystem
from Elevator import ElevatorSystem

def main() -> None:
    """Main function"""
    NUMBER_OF_FLOORS = 7

    e1 = ElevatorSystem(idx=1, number_of_floors=NUMBER_OF_FLOORS)
    e1.press_elevator_button(3)

    e2 = ElevatorSystem(idx=2, number_of_floors=NUMBER_OF_FLOORS)

    floors = FloorSystem.generate_floors(NUMBER_OF_FLOORS)

    floors[2].call_elevator_from_floor(e2)


if __name__ == "__main__":
    main()
