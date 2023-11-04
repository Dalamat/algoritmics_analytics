import envs
import asyncio
from telegram import Bot


TOKEN = envs.telegram_bot_token
GROUP_ID = envs.telegram_group

async def send_group_message(text: str):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=GROUP_ID, text=text)

# Test function call
# asyncio.run(send_group_message("Test"+" "+"Test2"))