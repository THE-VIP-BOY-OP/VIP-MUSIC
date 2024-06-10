import logging


# Define a custom logging filter to ignore specific messages
class IgnoreSpecificErrors(logging.Filter):
    def filter(self, record):
        # Return False if the log message contains "ChatAdminRequired" or "ChannelPrivate", thus excluding them from logging
        return not any(
            err in record.getMessage()
            for err in ["ChatAdminRequired", "ChannelPrivate"]
        )


# Configure logging with basic settings
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(),
    ],
)

# Create an instance of the custom filter
filter = IgnoreSpecificErrors()

# List of loggers to apply the filter and set the logging level to ERROR
loggers_to_filter = ["httpx", "pyrogram", "pytgcalls", "pymongo", "ntgcalls"]

# Apply the filter and set the logging level for each specified logger
for logger_name in loggers_to_filter:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.ERROR)  # Set the logging level to ERROR
    logger.addFilter(filter)  # Add the custom filter to the logger


# Function to get a logger by name
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
