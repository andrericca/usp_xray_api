import logging

LOG_FORMAT = "[%(levelname)s] %(asctime)s: %(message)s"

logger = logging.getLogger()
if not logger.handlers:
    logger_handler = logging.StreamHandler()
    logger_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(logger_handler)
logger.setLevel(logging.INFO)
