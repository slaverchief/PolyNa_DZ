import asyncio
import logging
from random import randint
import handlers as h
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
import env

logging.basicConfig(level=logging.INFO)
bot = Bot(token=env.TOKEN)
dp = Dispatcher()
regdp = dp.message.register


regdp(h.start, Command('start'))

async def main():
    await dp.start_polling(bot, image_ids=[])


if __name__ == "__main__":
    asyncio.run(main())
