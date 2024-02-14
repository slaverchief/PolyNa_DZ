from aiogram.filters.command import Command
from aiogram import types
from aiogram import types


async def start(message: types.Message):
    await message.answer("Hello")