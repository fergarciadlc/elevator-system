from Floor import FloorSystem
from Elevator import ElevatorSystem

class ElevatorDispatcher:
    """ElevatorDispatcher:
    Determines which elevator sent to a requested floor
    """
    @staticmethod
    def _nearest_elevator(elevator_floor_list: list, floor_number: int) -> int:
        """Select the nearest elevator from list of elevators list"""
        elevator_id = min(elevator_floor_list, key=lambda x: abs(x - floor_number))
        return elevator_id

    @classmethod
    def request_elevator_from_floor(
        cls, floor_number: int, elevators_list: list
    ) -> ElevatorSystem:
        """Returns closest elevator from the called floor number

        object contruction to use only one elevator by floor, ignore duplicates
        {
            "floor_number": "last_elevator_instance_in_floor",
            ...
        }
        """
        elevators_by_floor = {}
        for elevator in elevators_list:
            elevators_by_floor[elevator.current_floor] = elevator

        floor_by_elevator_list = sorted(elevators_by_floor.keys())

        closest_floor_elevator = cls._nearest_elevator(
            floor_by_elevator_list, floor_number
        )

        return elevators_by_floor[closest_floor_elevator]


"""
floors[2].call_elevator_from_floor(dispatcher.request_elevator_from_floor(2, [e1,e2]))
"""


if __name__ == "__main__":
    NUMBER_OF_FLOORS = 7

    e1 = ElevatorSystem(idx=1, number_of_floors=NUMBER_OF_FLOORS)
    e1.press_elevator_button(3)

    e2 = ElevatorSystem(idx=2, number_of_floors=NUMBER_OF_FLOORS)

    floors = FloorSystem.generate_floors(NUMBER_OF_FLOORS)

    floors[2].call_elevator_from_floor(e2)

    # dispatcher
    dispatcher = ElevatorDispatcher()

    # works!!!
    requested_floor = 4
    floors[requested_floor].call_elevator_from_floor(
        dispatcher.request_elevator_from_floor(requested_floor, [e1, e2])
    )
