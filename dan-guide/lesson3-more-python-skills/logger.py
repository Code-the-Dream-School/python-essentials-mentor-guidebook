# logging.py
import logging
from functools import wraps

# Setup logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# File handler
fh = logging.FileHandler("app.log")
fh.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

# Logging levels
logger.debug("Debug message (won't show in console)")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

# Example of logging in a function
def divide(a, b):
    logger.info(f"Dividing {a} by {b}")
    try:
        return a / b
    except ZeroDivisionError as e:
        logger.exception("Tried dividing by zero!")
        return None

# Example of logging via decorator
def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Calling: {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_function_call
def multiply(a, b):
    return a * b

# Trigger the functions
divide(10, 2)
divide(10, 0)
multiply(4, 5)
