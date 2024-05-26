import requests
import time
import os
import sys
import logging
from logging import StreamHandler

def setup_logger():
    log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    # Setup handler for messages
    message_handler = StreamHandler(sys.stdout)
    message_handler.setFormatter(log_formatter)
    message_handler.addFilter(lambda record: record.levelno <= logging.INFO)
    message_handler.setLevel(logging.DEBUG)

    # Setup handler for errors
    error_handler = StreamHandler(sys.stderr)
    error_handler.setFormatter(log_formatter)
    error_handler.setLevel(logging.WARNING)

    # Setup logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(message_handler)
    logger.addHandler(error_handler)
    return logger

def start_heartbeat(url, period, timeout, logger):
    while True:
        try:
            logger.info(f"Sending request to {url}")
            response = requests.get(url, timeout=timeout)
            logger.info(f"Response from {url}: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
        time.sleep(period)

if __name__ == "__main__":
    # Setup logger
    logger = setup_logger()

    # Get environment variables
    url = os.getenv("URL")
    if not url:
        logger.error("URL environment variable is required")
        sys.exit(1)

    period = int(os.getenv("PERIOD", "60"))
    timeout = float(os.getenv("TIMEOUT", "2.0"))

    logger.info(f"Starting heartbeat to {url} every {period} seconds with a timeout of {timeout} seconds.")

    # Start heartbeat
    start_heartbeat(url, period, timeout, logger)
