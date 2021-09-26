from Button import HallButtons
from Elevator import ElevatorSystem
import Log as log

logger = log.setup_logger()


class Floor:
    """Generic floor class

    Attributes:
        _floor_number (int): Floor number
        buttons (list): List of hall buttons
    """

    def __init__(self, floor_number: int) -> None:
        self._floor_number = floor_number
        self.buttons = HallButtons.generate_hall_buttons()

    @classmethod
    def generate_floors(cls, number_of_floors: int) -> list:
        """Generate a list of floors for building

        Args:
            number_of_floors (int): Number of floors

        Returns:
            list: List of Floor instances
        """
        return [cls(n) for n in range(number_of_floors)]

    def __repr__(self) -> str:
        return f"Floor {self._floor_number}: {self.buttons}"


class FloorSystem(Floor):
    """Floor Logic interface for Elevator System, inherits from Floor

    Args:
        Floor (Floor): Current Floor object
    """

    def __init__(self, floor_number: int) -> None:
        super().__init__(floor_number)

    def call_elevator_from_floor(self, elevator_system: ElevatorSystem) -> None:
        """Call elevator from current floor

        Args:
            elevator_system (ElevatorSystem): Elevator system called from floor

        Raises:
            Exception: If elevator_system is not an instance of ElevatorSystem
        """
        if not isinstance(elevator_system, ElevatorSystem):
            raise Exception(f"{elevator_system} is not an instance of {ElevatorSystem}")
        logger.info(f"Elevator requested from floor {self._floor_number}")
        self.buttons.press_button()
        logger.info(f"Floor button {self.buttons}")
        elevator_system.request_floor(self._floor_number)
        self.buttons.deactivate()
        logger.info(f"Floor button {self.buttons}")

    def __repr__(self) -> str:
        return super().__repr__()


if __name__ == "__main__":
    f = Floor(2)
    fs = Floor.generate_floors(5)
    f_sys = FloorSystem.generate_floors(3)
