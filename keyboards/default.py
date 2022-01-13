from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
# from data_fetcher.data_fetcher import times
manzil = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text='manzilni yuborish',request_location=True))
#
# async def timess(lat,long):
#     a = await times(lat=lat,long=long)
#     data = a['data']
#     numbers = 1
#     mark = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
#     for num in data:
#         mark.insert(KeyboardButton(text=f'{numbers}'))
#         numbers += 1
#     mark.insert(KeyboardButton('orqaga'))
#     return mark
startt = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/start'))
tasdiq = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
tasdiq.insert(KeyboardButton(text='/bugungi'))
tasdiq.insert(KeyboardButton(text='/ertangi'))
tasdiq.insert(KeyboardButton(text='/3kunlig'))