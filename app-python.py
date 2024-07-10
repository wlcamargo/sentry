import logging
from configs import setup_sentry

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")

try:
    1 / 0
except ZeroDivisionError as e:
    logger.exception("An exception occurred")