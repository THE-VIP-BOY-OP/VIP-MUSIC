import logging


# Custom logging filter to ignore specific messages
class IgnoreChatAdminRequired(logging.Filter):
    def filter(self, record):
        return "ChatAdminRequired" not in record.getMessage()


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(),
    ],
)

# Create a filter instance
filter = IgnoreChatAdminRequired()

# Apply the filter to relevant loggers
loggers_to_filter = ["httpx", "pyrogram", "pytgcalls", "pymongo", "ntgcalls"]

for logger_name in loggers_to_filter:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.ERROR)
    logger.addFilter(filter)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
