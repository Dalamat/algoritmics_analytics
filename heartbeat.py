from telegram_client import send_group_message
import asyncio
from log_config import logger


def heartbeat():
    message = "Update service is up and running"
    logger.info(message)
    asyncio.run(send_group_message(message))

# heartbeat()