from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menuMain = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇷🇺Rus tili"),
            KeyboardButton(text="🇺🇿Ozbek tili")
        ]
      
    ],
    resize_keyboard=True
)

menuButtons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📄Ma'lumot")
        ],
        [
            KeyboardButton(text="👨‍💻Xodimlar haqida ma'lumot")
        ],
        [
            KeyboardButton(text="Nima yordam bera olaman😇")
        ],
        [
                KeyboardButton(text="Tilni o'zgartirish🇷🇺"),
                KeyboardButton(text= "📄Savolar")
        ]
    ],
   resize_keyboard=True
)

