import logging
import datetime
import time
from functools import wraps

# TS = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
TS = datetime.datetime.now().strftime('%Y%m%d')
formatter = logging.Formatter(
    '%(asctime)s, %(levelname)s, %(filename)s, %(funcName)s: %(message)s')


def logger(name: str, log_file_name: str = "", level=logging.INFO):
    log_file = f"./logs/app_logger_{TS}.log"

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger_custom = logging.getLogger(name)
    logger_custom.setLevel(level)
    logger_custom.addHandler(file_handler)
    logger_custom.addHandler(stream_handler)

    return logger_custom
# Create a logger instance
_app_logger = logger(__name__)

def log_execution_time(func):
    """
    A decorator to log the start and end times of a function or method.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        _app_logger.info(f"Starting: {func.__qualname__}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        _app_logger.info(f"Finished: {func.__qualname__} (Elapsed Time: {elapsed_time:.4f}s)")
        return result

    return wrapper
