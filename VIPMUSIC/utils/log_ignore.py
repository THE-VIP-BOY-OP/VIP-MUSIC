import logging

class IgnoreSpecificErrors(logging.Filter):
    def filter(self, record):
        # Specify the error messages to ignore
        error_messages_to_ignore = [
            "pyrogram.errors.exceptions.forbidden_403.ChatWriteForbidden: Telegram says: [403 CHAT_WRITE_FORBIDDEN] - You don't have rights to send messages in this chat (caused by \"messages.SendMessage\")",
            "Error: Telegram says: [400 CHAT_ADMIN_REQUIRED] - The method requires chat admin privileges (caused by \"messages.ExportChatInvite\")",
            "pyrogram.errors.exceptions.not_acceptable_406.ChannelPrivate: Telegram says: [406 CHANNEL_PRIVATE] - The channel/supergroup is not accessible (caused by \"channels.GetFullChannel\")"
        ]
        
        # Return False if the log message matches any of the specified error messages, thus excluding it from logging
        return not any(err in record.getMessage() for err in error_messages_to_ignore)

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
