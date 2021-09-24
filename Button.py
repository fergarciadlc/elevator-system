from enum import Enum


class Button:
    # status is equivalent to indicator led light
    def __init__(self) -> None:
        self.status = False

    def _toggle_status(self) -> None:
        self.status = not self.status

    def press_button(self) -> None:
        # self._toggle_status() ## original, user controls on and off
        ## do I want to emulate one press??
        if not self.is_pressed:
            self._toggle_status()

    @property
    def is_pressed(self) -> bool:
        return self.status

    def deactivate(self) -> None:
        if self.status is not False:
            self._toggle_status()

    def __repr__(self) -> str:
        return f"Generic Button: {self.status}"


class ElevatorButton(Button):
    def __init__(self, floor_number: int) -> None:
        super().__init__()
        self.floor_number = floor_number

    def double_press(self) -> None:
        if self.is_pressed:
            self.deactivate()

    @classmethod
    def from_number_of_floors(cls, number_of_floors: int) -> list:
        return [cls(n) for n in range(number_of_floors)]

    def __repr__(self) -> str:
        return f"Elevator button number {self.floor_number}: {self.status}"


class ButtonDirection(Enum):
    UP = 1
    DOWN = 2
    CALL = 3


class HallButtons(Button):
    def __init__(self, direction: ButtonDirection) -> None:
        super().__init__()
        self.direction = direction

    @classmethod
    def generate_hall_buttons(cls) -> dict:
        # return {"UP": cls(ButtonDirection.UP), "DOWN": cls(ButtonDirection.DOWN)}
        return cls(ButtonDirection.CALL)


    def __repr__(self) -> str:
        return f"Hall Button {self.direction}: {self.status}"


if __name__ == "__main__":
    b = Button()
    e = ElevatorButton.from_number_of_floors(7)
    h = HallButtons.generate_hall_buttons()
