from loguru import logger
import sys
import os

# Ensure logs directory exists
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Remove default logger
logger.remove()

# Console logging
logger.add(
    sys.stdout,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
    colorize=True
)

# File logging
logger.add(
    os.path.join(LOG_DIR, "app.log"),
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    rotation="1 MB",        # rotate after 1MB
    retention="7 days",     # keep logs for 7 days
    compression="zip",      # compress old logs
    level="INFO"
)

# Optional: error-only log file
logger.add(
    os.path.join(LOG_DIR, "error.log"),
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="ERROR"
)