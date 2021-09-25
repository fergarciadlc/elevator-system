import logging

root_logger = logging.getLogger("app")
root_logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    fmt="%(asctime)s - [%(filename)s:%(lineno)s - %(funcName)s ] - %(levelname)s - %(message)s"
)
file_handler = logging.FileHandler("elevator_system.log")
file_handler.setFormatter(formatter)

handler = logging.StreamHandler()
handler.setFormatter(formatter)
initialized = False
if not initialized:
    root_logger.addHandler(handler)
    root_logger.addHandler(file_handler)
    initialized = True


def setup_logger() -> logging.Logger:
    logger = logging.getLogger(f"app.{__name__}")
    logger.setLevel(logging.DEBUG)
    return logger
