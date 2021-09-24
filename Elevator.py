from Button import ElevatorButton
from Motor import Motor, MotorState
from Door import Door
import time


class Elevator:
    def __init__(self, idx: int, number_of_floors: int) -> None:
        self.idx = idx
        self.buttons = ElevatorButton.from_number_of_floors(number_of_floors)
        self.motor = Motor()
        self.door = Door()
        self.current_floor = self.buttons[0].floor_number

    def open_and_close_door(self) -> None:
        if self.motor.state is not MotorState.IDLE:
            raise Exception("Doors cannot open, elevator moving.")
        self.door.open_door()
        print(self.door)
        time.sleep(1)
        self.door.close_door()
        print(self.door)

    def move_one_floor(self, direction: MotorState) -> None:
        str_direction_identifier = direction.name
        direction_mapping = {
            MotorState.UP: (-1, "final"),
            MotorState.DOWN: (0, "inital"),
        }
        if self.door.is_open:
            raise Exception(
                f"Elevator cannot go {str_direction_identifier}, {self.door}."
            )
        if (
            self.current_floor
            is self.buttons[direction_mapping[direction][0]].floor_number
        ):
            raise Exception(
                f"Elevator cannot go {str_direction_identifier}, {direction_mapping[direction][-1]} floor."
            )
        self.motor.set_state(direction)
        print(f"Elevator motor: {self.motor.state}")
        time.sleep(0.5)

        if direction is MotorState.UP:
            self.current_floor += 1
        elif direction is MotorState.DOWN:
            self.current_floor -= 1
        self.motor.set_state(MotorState.IDLE)
        print(f"Elevator motor: {self.motor.state}")

    def __repr__(self) -> str:
        return (
            f"[ Elevator ID ]: {self.idx}"
            + f"\n[Current Floor]: {self.current_floor}"
            + f"\n[    State    ]: {self.motor}"
            + f"\n[    Door     ]: {self.door}"
            + f"\n[Total of floors with Ground Level]: {len(self.buttons)}"
        )


class ElevatorSystem(Elevator):
    def __init__(self, idx: int, number_of_floors: int) -> None:
        super().__init__(idx, number_of_floors)

        self.floors_list = tuple([button.floor_number for button in self.buttons])

    def request_floor(self, requested_floor_number: int):
        if requested_floor_number not in self.floors_list:
            raise Exception(
                f"Invalid requested floor: {requested_floor_number}, Elevator available floors: {self.floors_list}"
            )

        if self.current_floor < requested_floor_number:
            direction = MotorState.UP
        else:
            direction = MotorState.DOWN

        while requested_floor_number != self.current_floor:
            self.move_one_floor(direction)

        self.open_and_close_door()

    def press_elevator_button(self, pressed_button: int):
        if pressed_button not in self.floors_list:
            raise Exception(f"Invallid requested button: {pressed_button}")
        self.buttons[pressed_button].press_button()
        print(self.buttons[pressed_button])
        self.request_floor(pressed_button)
        self.buttons[pressed_button].deactivate()
        print(self.buttons[pressed_button])


    def emergency_stop(self):
        self.motor.set_state(MotorState.IDLE)
        self.door.open_door()
        print("\n\nEMERGENCY STOP \n\n" + super().__repr__())
        return False

    def __repr__(self) -> str:
        return super().__repr__()


if __name__ == "__main__":
    # e = Elevator(idx=1, number_of_floors=5)
    # e.move_one_floor(MotorState.UP)

    es = ElevatorSystem(idx=1, number_of_floors=5)
    es.request_floor(3)
