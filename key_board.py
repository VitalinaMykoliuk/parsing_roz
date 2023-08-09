from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/start"))

'''Главное меню'''

main_menu_2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Мой профиль', callback_data='Мой профиль'),
     InlineKeyboardButton('Раздел товаров', callback_data='Раздел')]
])


'''Меню для роздела товаров'''

main_menu_category = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Игровые ПК', callback_data='ПК'),
     InlineKeyboardButton('Телефоны', callback_data='Телефоны'),
     ],
    [
     InlineKeyboardButton('Утюги', callback_data='Утюги'),
     InlineKeyboardButton('Рюкзаки', callback_data='Рюкзаки')
    ]
])


'''Машинное состояние, кнопка назад'''

main_back = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('back'))