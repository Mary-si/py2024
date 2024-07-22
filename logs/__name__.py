import logging
from enum import Enum


class LogLevel(Enum):
    DEBUG = logging.DEBUG  # 10
    INFO = logging.INFO  # 20
    WARNING = logging.WARNING  # 30
    ERROR = logging.ERROR  # 40
    CRITICAL = logging.CRITICAL  # 50


def setup_logger(name: str, level: LogLevel, log_file: str) -> logging.Logger:
    # Create a named logger
    logger = logging.getLogger(f"__{name}__")
    logger.setLevel(level.value)  # Set logger level using enum value

    # Create a console handler and set its level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level.value)

    # Create a file handler and set its level
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level.value)

    # Set the formatter for both handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S%p",
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
