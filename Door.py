class Door:
    # Opened -> True
    # Closed -> Flase
    def __init__(self) -> None:
        self.status = False

    def _toggle_status(self) -> None:
        self.status = not self.status

    def open_door(self) -> None:
        if not self.is_open:
            self._toggle_status()

    def close_door(self) -> None:
        if self.is_open:
            self._toggle_status()

    @property
    def is_open(self) -> bool:
        return self.status

    def __repr__(self) -> str:
        status_str = "Open" if self.is_open else "Close"
        return f"Door is: {status_str}"


if __name__ == "__main__":
    d = Door()
    