from aiogram.filters.command import Command
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

async def maps_library(message: types.Message):
    await message.answer("https://mospolynavigation.github.io/dod/")

async def new_route(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Официальная часть",
        callback_data="of_part")
    )
    await message.answer(
        "Нажмите на кнопку, если ваше имя - София",
        reply_markup=builder.as_markup()
    )

async def start(message: types.Message, image_ids: dict):
    image_id = image_ids.get('to_load', None)
    to_load = None
    print(image_id)
    if image_id:
        print('got')
        await message.answer_photo(photo=image_id, caption="То что я люблю")
    else:
        img = types.FSInputFile('to_load.jpeg')
        res = await message.answer_photo(photo=img, caption="То что я люблю")
        image_ids['to_load'] = res.photo[-1].file_id
    kb = [
        [types.KeyboardButton(text="Новый маршрут")],
        [types.KeyboardButton(text="Библиотека карт")]
    ]
    kb = types.ReplyKeyboardMarkup(keyboard=kb,
                                   input_field_placeholder="Ответ вводить тут",
                                   resize_keyboard=True)
    await message.answer(text="Что вам нужно?", reply_markup=kb)

