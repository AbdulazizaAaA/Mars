from aiogram import types, Bot, executor, Dispatcher
from data import Api_token
import logging
from buttons import menuMain
from buttons import menuButtons

bot = Bot(Api_token)
dp = Dispatcher(bot)

# --> Kimdur kirganlik haqida ma'lumot beruvchi
logging.basicConfig(level=logging.INFO)



@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    username = message.from_user.full_name
    logging.info(message)
    await message.answer(f"Salom {username}", reply_markup=menuMain)


@dp.message_handler(text='🇺🇿Ozbek tili')
async def start(message:types.Message):
    await message.answer("Kerakli bolimni tanlang",reply_markup=menuButtons)

dp.message_handler(text="📄Ma'lumot")
async def start(message:types.Message):
    await message.answer("Bizning Malumot",reply_markup=menuButtons)
    await message.answer_photo("https://t.me/python_9_00/600")
    await message.answer_photo("https://t.me/python_9_00/582")





if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


