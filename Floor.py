from Button import HallButtons
from Elevator import ElevatorSystem


class Floor:
    def __init__(self, floor_number: int) -> None:
        self._floor_number = floor_number
        self.buttons = HallButtons.generate_hall_buttons()

    @classmethod
    def generate_floors(cls, number_of_floors: int) -> list:
        return [cls(n) for n in range(number_of_floors)]

    def __repr__(self) -> str:
        return f"Floor {self._floor_number}: {self.buttons}"


class FloorSystem(Floor):
    def __init__(self, floor_number: int) -> None:
        super().__init__(floor_number)

    def call_elevator_from_floor(self, elevator_system: ElevatorSystem) -> None:
        if not isinstance(elevator_system, ElevatorSystem):
            raise Exception(
                f"{elevator_system} is not an instance of {ElevatorSystem}"
            )
        self.buttons.press_button()
        elevator_system.request_floor(self._floor_number)
        self.buttons.deactivate()

    def __repr__(self) -> str:
        return super().__repr__()

if __name__ == "__main__":
    f = Floor(2)
    fs = Floor.generate_floors(5)
    f_sys = FloorSystem.generate_floors(3)