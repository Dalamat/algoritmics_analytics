from telegram_client import send_group_message
import asyncio


def heartbeat():
    message = "Update service is up and running"
    print(message)
    asyncio.run(send_group_message(message))

# heartbeat()