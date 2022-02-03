import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

LOGGER_NAME = "FRAMEWORK_DESAFIO"


def create_logger():
    if not os.path.exists("./logs"):
        os.makedirs("./logs")

    logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG)

    handler_local = RotatingFileHandler(
        f"./logs/log.log", mode="a", maxBytes=50000, backupCount=10
    )
    formatter = logging.Formatter(
        "[%(levelname)s] %(asctime)s %(funcName)s -> %(message)s"
    )

    handler_local.setFormatter(formatter)
    logger.addHandler(handler_local)

    return logger


def get_logger():
    logger = logging.getLogger(LOGGER_NAME)
    return logger


def trace_logger(func):
    """
    This function trace the begin timestamp, the end timestamp, thee execution_time, the raw return and the status_code
    """
    def inner(*args, **kwargs):
        logger = get_logger()

        begin_timestamp = datetime.now()
        logger.info(f"Timestamp begin -> {begin_timestamp}\n")

        func_response = func(*args, **kwargs)

        end_timestamp = datetime.now()

        logger.info(f"Timestamp End -> {end_timestamp}")
        logger.info(f"Execution time -> {end_timestamp - begin_timestamp}")
        logger.info(f"Json raw -> {func_response.json}")
        logger.info(f"status_code -> {func_response.status_code}\n")
        return func_response

    return inner
