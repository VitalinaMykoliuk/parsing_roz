from aiogram import types, executor, Dispatcher, Bot
from dotenv import dotenv_values
import key_board
from key_board import main_menu_2, main_menu_category, main_back
import asyncio
import requests
from bs4 import BeautifulSoup
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


storage = MemoryStorage()

logging.basicConfig(level=logging.INFO)


config = dotenv_values('.env')
bot = Bot(config['token'])
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands='start')
async def start(message: types.message):
    await message.answer(f'Привет <a href="{message.from_user.url}">{message.from_user.first_name}'
                         f'</a> я бот для поиска товаров на сайте', parse_mode='html')

    await asyncio.sleep(3)
    await message.answer('Главное меню', reply_markup=key_board.main_menu_2)


@dp.callback_query_handler(lambda x: x.data == 'Раздел')
async def section(callback: types.CallbackQuery):
    await callback.message.answer('Категории товаров', reply_markup=main_menu_category)


@dp.callback_query_handler(lambda y: y.data == 'ПК')
async def game_pk(callback: types.CallbackQuery):
    await storage.set_state(chat=callback.from_user.id, state='check')
    await storage.update_data(chat=callback.from_user.id, data={'pk_game': True})
    await callback.message.answer('Начинаю парсинг', reply_markup=main_back)
    url = "https://hard.rozetka.com.ua/computers/c80095/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    page_count = int(soup.find("div", class_="pagination ng-star-inserted").find_all("li",
                                                                     class_="ng-star-inserted")[-1].text.strip())

    print(f"Всего страниц: {page_count}")
    for page in range(1, page_count + 1):
        logging.info(f'Обработка {page} страницы')
        url = f"https://hard.rozetka.com.ua/computers/c80095/page={page}/"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")

        items = soup.find_all("li", class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
        for item in items:
            try:
                data = await storage.get_data(chat=callback.from_user.id)
                if not data.get('pk_game'):
                    await callback.message.answer('Выберете меню товаров', reply_markup=main_menu_category)
                    return
                title = item.find('a', class_='goods-tile__heading ng-star-inserted').text.strip()
                image = item.find('a', class_='goods-tile__picture ng-star-inserted').get('href').strip()
                link = item.find('a', class_='goods-tile__heading')['href']
                price = item.find('div', class_='goods-tile__prices').find('p', class_='ng-star-inserted').text.strip()
                status = item.find('div', class_='goods-tile__availability').text.strip()
                await asyncio.sleep(2)
                await bot.send_photo(callback.from_user.id, image, caption="<b>" + title + "</b>\n<i>" +
                    price + "</i>\n<i>" + status + f"</i>\n<a href='{link}'>Ссылка на товар</a>",  parse_mode='html')

            except:
                ValueError()


@dp.message_handler(state='check')
async def check(message: types.Message, state):
    if message.text == 'back':
        await state.update_data({'pk_game': False})
        await state.finish()


@dp.callback_query_handler(lambda a: a.data == 'Телефоны')
async def telephone(callback: types.CallbackQuery):
    await storage.set_state(chat=callback.from_user.id, state='check')
    await storage.update_data(chat=callback.from_user.id, data={'telephones': True})
    await callback.message.answer('Начинаю парсинг', reply_markup=main_back)
    url = "https://rozetka.com.ua/mobile-phones/c80003/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    page_count = int(soup.find("div", class_="pagination ng-star-inserted").find_all("li",
                                                                    class_="ng-star-inserted")[-1].text.strip())

    print(f"Всего страниц: {page_count}")
    for page in range(1, page_count + 1):
        logging.info(f'Обработка {page} страницы')
        url = f"https://rozetka.com.ua/mobile-phones/c80003/page={page}/"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")

        items = soup.find_all("li", class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
        for item in items:
            try:
                data = await storage.get_data(chat=callback.from_user.id)
                if not data.get('telephones'):
                    await callback.message.answer('Выберете меню товаров', reply_markup=main_menu_category)
                    return
                title = item.find('a', class_='goods-tile__heading ng-star-inserted').text.strip()
                image = item.find('a', class_='goods-tile__picture ng-star-inserted').get('href').strip()
                link = item.find('a', class_='goods-tile__heading')['href']
                price = item.find('div', class_='goods-tile__prices').find('p', class_='ng-star-inserted').text.strip()
                status = item.find('div', class_='goods-tile__availability').text.strip()
                await asyncio.sleep(2)
                await bot.send_photo(callback.from_user.id, image, caption="<b>" + title + "</b>\n<i>" +
                     price + "</i>\n<i>" + status + f"</i>\n<a href='{link}'>Ссылка на товар</a>", parse_mode='html')

            except:
                ValueError()


@dp.message_handler(state='check')
async def check(message: types.Message, state):
    if message.text == 'back':
        await state.update_data({'telephones': False})
        await state.finish()


@dp.callback_query_handler(lambda b: b.data == 'Утюги')
async def iron(callback: types.CallbackQuery):
    await storage.set_state(chat=callback.from_user.id, state='check')
    await storage.update_data(chat=callback.from_user.id, data={'irons': True})
    await callback.message.answer('Начинаю парсинг', reply_markup=main_back)
    url = "https://bt.rozetka.com.ua/irons/c80161/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    page_count = int(soup.find("div", class_="pagination ng-star-inserted").find_all("li",
                                                                 class_="ng-star-inserted")[-1].text.strip())

    print(f"Всего страниц: {page_count}")
    for page in range(1, page_count + 1):
        logging.info(f'Обработка {page} страницы')
        url = f"https://bt.rozetka.com.ua/irons/c80161/page={page}/"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")

        items = soup.find_all("li", class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
        for item in items:
            try:
                data = await storage.get_data(chat=callback.from_user.id)
                if not data.get('irons'):
                    await callback.message.answer('Выберете меню товаров', reply_markup=main_menu_category)
                    return
                title = item.find('a', class_='goods-tile__heading ng-star-inserted').text.strip()
                image = item.find('a', class_='goods-tile__picture ng-star-inserted').get('href').strip()
                link = item.find('a', class_='goods-tile__heading')['href']
                price = item.find('div', class_='goods-tile__prices').find('p', class_='ng-star-inserted').text.strip()
                status = item.find('div', class_='goods-tile__availability').text.strip()
                await asyncio.sleep(2)
                await bot.send_photo(callback.from_user.id, image, caption="<b>" + title + "</b>\n<i>" +
                     price + "</i>\n<i>" + status + f"</i>\n<a href='{link}'>Ссылка на товар</a>", parse_mode='html')

            except:
                ValueError()


@dp.message_handler(state='check')
async def check(message: types.Message, state):
    if message.text == 'back':
        await state.update_data({'irons': False})
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == 'Рюкзаки')
async def backpack(callback: types.CallbackQuery):
    await storage.set_state(chat=callback.from_user.id, state='check')
    await storage.update_data(chat=callback.from_user.id, data={'backpacks': True})
    await callback.message.answer('Начинаю парсинг', reply_markup=main_back)
    url = "https://rozetka.com.ua/ryukzaki4630377/c4630377/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    page_count = int(soup.find("div", class_="pagination ng-star-inserted").find_all("li",
                                                              class_="ng-star-inserted")[-1].text.strip())

    print(f"Всего страниц: {page_count}")
    for page in range(1, page_count + 1):
        logging.info(f'Обработка {page} страницы')
        url = f"https://rozetka.com.ua/ryukzaki4630377/c4630377/page={page}/"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")

        items = soup.find_all("li", class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
        for item in items:
            try:
                data = await storage.get_data(chat=callback.from_user.id)
                if not data.get('backpacks'):
                    await callback.message.answer('Выберете меню товаров', reply_markup=main_menu_category)
                    return
                title = item.find('a', class_='goods-tile__heading ng-star-inserted').text.strip()
                image = item.find('a', class_='goods-tile__picture ng-star-inserted').get('href').strip()
                link = item.find('a', class_='goods-tile__heading')['href']
                price = item.find('div', class_='goods-tile__prices').find('p', class_='ng-star-inserted').text.strip()
                status = item.find('div', class_='goods-tile__availability').text.strip()
                await asyncio.sleep(2)
                await bot.send_photo(callback.from_user.id, image, caption="<b>" + title + "</b>\n<i>" +
                  price + "</i>\n<i>" + status + f"</i>\n<a href='{link}'>Ссылка на товар</a>", parse_mode='html')

            except:
                ValueError()


@dp.message_handler(state='check')
async def check(message: types.Message, state):
    if message.text == 'back':
        await state.update_data({'backpacks': False})
        await state.finish()


executor.start_polling(dp)
