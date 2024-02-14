import asyncio
import logging
from random import randint
import handlers as h
import callbacks as c
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command, CommandObject
import env

logging.basicConfig(level=logging.INFO)
bot = Bot(token=env.TOKEN)
dp = Dispatcher()
regdp = dp.message.register
regcb = dp.callback_query.register

regcb(c.answer_of_button, F.data == "of_part")
regdp(h.start, Command('start'))
regdp(h.new_route, F.text.lower() == "новый маршрут")
regdp(h.maps_library, F.text.lower() == "библиотека карт")

async def main():
    await dp.start_polling(bot, image_ids={})


if __name__ == "__main__":
    asyncio.run(main())
