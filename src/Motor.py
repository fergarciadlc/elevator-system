from enum import Enum


class MotorState(Enum):
    IDLE = 0
    UP = 1
    DOWN = 2


class Motor:
    """Generig elevator motor with states.

    Attributes:
        state (MotorState): Current state of motor

    States:
        IDLE: Motor not moving
        UP: Motor moving up
        DOWN: Motor moving down.
    """

    def __init__(self, motor_state: MotorState = MotorState.IDLE) -> None:
        self.state = motor_state

    def set_state(self, motor_state) -> None:
        """Change current state of motor

        Args:
            motor_state (MotorState): Motor states

        Raises:
            Exception: If state is not in current defined states
        """
        if not isinstance(motor_state, MotorState):
            raise Exception(
                f"{type(motor_state)} is not an instance of {type(MotorState)}"
            )
        self.state = motor_state

    def stop(self) -> None:
        """Stops motor"""
        self.state = MotorState.IDLE

    def __repr__(self) -> str:
        return f"Motor state: {self.state.name}"


if __name__ == "__main__":
    m = Motor()
