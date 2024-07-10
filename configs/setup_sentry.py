import logging
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
from dotenv import load_dotenv
import os

load_dotenv()

dsn = os.getenv('DSN')

sentry_logging = LoggingIntegration(
    level=logging.INFO,       
    event_level=logging.ERROR
)

sentry_sdk.init(
    dsn=dsn,
    integrations=[sentry_logging]
)