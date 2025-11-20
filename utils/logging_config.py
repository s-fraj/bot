from loguru import logger

def setup_logging():
    logger.add("logs/bot.log", rotation="1 MB")
