import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())