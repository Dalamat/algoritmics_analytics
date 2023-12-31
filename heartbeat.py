from telegram_client import send_group_message
import asyncio
from log_config import logger
import envs


def heartbeat():
    message = f"Update service is up and running. ENV: {envs.environment}"
    logger.info(message)
    asyncio.run(send_group_message(message))

# heartbeat()