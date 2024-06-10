import logging

class IgnoreSpecificErrors(logging.Filter):
    def filter(self, record):
        # Specify the error message to ignore
        error_message_to_ignore = "pyrogram.errors.exceptions.forbidden_403.ChatWriteForbidden: Telegram says: [403 CHAT_WRITE_FORBIDDEN] - You don't have rights to send messages in this chat (caused by \"messages.SendMessage\")"
        
        # Return False if the log message matches the specified error message, thus excluding it from logging
        return error_message_to_ignore not in record.getMessage()

# Add this custom filter to your logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(),
    ],
    filters=[IgnoreSpecificErrors()]
)
