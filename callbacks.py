from aiogram import types

async def answer_of_button(callback: types.CallbackQuery):
    await callback.message.answer("Good dog!")