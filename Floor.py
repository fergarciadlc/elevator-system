from Button import HallButtons


class Floor:
    def __init__(self, floor_number: int) -> None:
        self._floor_number = floor_number
        self.buttons = HallButtons.generate_hall_buttons()

    @classmethod
    def generate_floors(cls, number_of_floors: int) -> list:
        return [cls(n) for n in range(number_of_floors)]

    def __repr__(self) -> str:
        return f"Floor {self._floor_number}: {self.buttons}"


if __name__ == "__main__":
    f = Floor(2)
    fs = Floor.generate_floors(5)
