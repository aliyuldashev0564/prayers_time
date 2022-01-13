import datetime
from loader import db
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import bot
from state.state import States
from data_fetcher.data_fetcher import times
from keyboards import default
@db.message_handler(text='orqaga',state='*')
async def orqaga(msg: Message, state:FSMContext):
    await state.finish()
    await bot.send_message(msg.chat.id,'siz botni to`xtatingiz\n qayta ishgaa tushurush uchun 🔲start🔲 \ntugmasini bosing', reply_markup=default.startt)
@db.message_handler(text='about',state='*')
async def orqaga(msg: Message, state:FSMContext):
    await state.finish()
    await bot.send_message(msg.chat.id,''' bu bot @aliyuldashev0526 tomonidan yaratilgan 
malumotlar: Muslim World League(MAKKA, SAUDIYA ARABISTONI)
tashkilotidan olingan
''')
@db.message_handler(Command('start'), state='*')
async def start(msg:Message):
    await bot.send_message(msg.chat.id, f'Assalomu aleykum \n'
                                        f'namoz vaqtlarini bilish uchun\n'
                                        f'🔲manzilyi yuborish🔲\ntugmasini bosing\n yoki lokatsiya tashlang', reply_markup=default.manzil)
    await States.locat.set()
@db.message_handler(content_types=['location'], state=States.locat)
async def locatio(msg:Message, state:FSMContext):
    longitude = msg.location.longitude
    await States.next()
    latitude = msg.location.latitude
    await state.update_data({'long':f'{longitude}',
                             'lat':f"{latitude}"})
    await bot.send_message(msg.chat.id,'qaysi 🕰kun kerakligini tanlang' , reply_markup=default.tasdiq)
@db.message_handler(Command('bugungi'),state=States.day)
async def day(msg:Message,state:FSMContext):
    day = datetime.datetime.today().day
    data = await state.get_data()
    lat = data['lat']
    long = data['long']
    a = await times(lat=lat,long=long)
    num = 1
    message = ''
    for data1 in a['data']:
        if int(day) ==int(num):
            message = f'📆MILODIY: {data1["date"]["gregorian"]["date"]}\n📆XIJRIY {data1["date"]["hijri"]["date"]} \n' \
                      f'{"uchun namoz vaqtlari".upper()}\n' \
                      f'➖➖➖➖➖➖➖➖➖➖➖➖\n'
            timesss = data1['timings']
            for alpha,beta in timesss.items():
                if (alpha).upper() =='FAJR':
                    alpha = 'BOMDOD'
                if (alpha).upper() =='SUNRISE':
                    alpha = 'QUYOSH'
                if (alpha).upper() =='DHUHR':
                    alpha = 'PESHIN'
                if (alpha).upper() =='ASR':
                    alpha = 'ASR'
                if (alpha).upper() =='SUNSET':
                    alpha = 'QUYOSH botishi'
                if (alpha).upper() =='MAGHRIB':
                    alpha = 'SHOM'
                if (alpha).upper() =='ISHA':
                    await state.update_data({'xufton':beta[0:5]})
                    continue
                if (alpha).upper() =='IMSAK':
                    mal = await state.get_data()
                    xufton = mal['xufton']
                    message += f'⏳ XUFTON: {xufton} dan  {beta[0:5]} gacha\n'
                    continue
                if (alpha).upper() =='MIDNIGHT':
                    alpha = 'TAHAJUT'
                message += f'⏳ {alpha}:  {beta[0:5]}\n'
        num += 1
    message += f'➖➖➖➖➖➖➖➖➖➖➖➖\n'\
               '🙏iltimos namoz vaqtlarini xar \n3⃣ 3 kunda almashtirib turing'
    await bot.send_message(msg.chat.id,message)
@db.message_handler(Command('ertangi'),state=States.day)
async def day(msg:Message,state:FSMContext):
    day = datetime.datetime.today().day
    data = await state.get_data()
    lat = data['lat']
    long = data['long']
    a = await times(lat=lat,long=long)
    num = 1
    message = ''
    nume = 0
    for data1 in a['data']:
        if int(day)+1 ==int(num):
            message = f'📆MILODIY: {data1["date"]["gregorian"]["date"]}\n📆XIJRIY {data1["date"]["hijri"]["date"]} \n' \
                      f'{"uchun namoz vaqtlari".upper()}\n' \
                      f'➖➖➖➖➖➖➖➖➖➖\n'
            timesss = data1['timings']
            for alpha,beta in timesss.items():
                if (alpha).upper() == 'FAJR':
                    alpha = 'BOMDOD'
                if (alpha).upper() == 'SUNRISE':
                    alpha = 'QUYOSH'
                if (alpha).upper() == 'DHUHR':
                    alpha = 'PESHIN'
                if (alpha).upper() == 'ASR':
                    alpha = 'ASR'
                if (alpha).upper() == 'SUNSET':
                    alpha = 'QUYOSH botishi'
                if (alpha).upper() == 'MAGHRIB':
                    alpha = 'SHOM'
                if (alpha).upper() == 'ISHA':
                    await state.update_data({'xufton': beta[0:5]})
                    continue
                if (alpha).upper() == 'IMSAK':
                    mal = await state.get_data()
                    xufton = mal['xufton']
                    message += f'⏳ XUFTON: {xufton} dan  {beta[0:5]} gacha\n'
                    continue
                if (alpha).upper() == 'MIDNIGHT':
                    alpha = 'TAHAJUT'
                message += f'⏳ {(alpha).upper()}:  {beta[0:5]}\n'
                nume += 1
        num += 1
    if nume ==0:
        message += 'ERTANGI KUN UCHUN MALUMOT YO\'Q ILTIMOS BUGUNGI MALUMOTDAN FOYDALANIB TURING. MALUMOTLAR ERTAGACHA TAYOR BO\'LADI\n'
    message += f'➖➖➖➖➖➖➖➖➖➖➖➖\n'\
               f'{"🙏iltimos".upper()} namoz vaqtlarini xar \n3⃣ 3 kunda almashtirib turing'
    await bot.send_message(msg.chat.id,message)
@db.message_handler(Command('3kunlig'),state=States.day)
async def day(msg:Message,state:FSMContext):
    day = datetime.datetime.today().day
    data = await state.get_data()
    lat = data['lat']
    long = data['long']
    a = await times(lat=lat,long=long)
    num = 1
    message = ''
    nume = 0
    for data1 in a['data']:
        if int(day) ==int(num) or int(day)+1 ==int(num) or int(day)+2 ==int(num):
            message += f'📆MILODIY: {data1["date"]["gregorian"]["date"]}\n📆XIJRIY {data1["date"]["hijri"]["date"]} \n' \
                       f'{"uchun namoz vaqtlari".upper()}\n' \
                       f'➖➖➖➖➖➖➖➖➖➖➖➖\n'
            timesss = data1['timings']
            for alpha,beta in timesss.items():
                if (alpha).upper() =='FAJR':
                    alpha = 'BOMDOD'
                if (alpha).upper() =='SUNRISE':
                    alpha = 'QUYOSH'
                if (alpha).upper() =='DHUHR':
                    alpha = 'PESHIN'
                if (alpha).upper() =='ASR':
                    alpha = 'ASR'
                if (alpha).upper() =='SUNSET':
                    alpha = 'QUYOSH botishi'
                if (alpha).upper() =='MAGHRIB':
                    alpha = 'SHOM'
                if (alpha).upper() =='ISHA':
                    await state.update_data({'xufton':beta[0:5]})
                    continue
                if (alpha).upper() =='IMSAK':
                    mal = await state.get_data()
                    xufton = mal['xufton']
                    message += f'⏳ XUFTON: {xufton} dan  {beta[0:5]} gacha\n'
                    continue
                if (alpha).upper() =='MIDNIGHT':
                    alpha = 'TAHAJUT'
                message += f'⏳  {(alpha).upper()}:  {beta[0:5]}\n'
            nume += 1
            message += '➖➖➖➖➖➖➖➖➖➖➖➖\n'
        num += 1
    if nume != 1:
        message = '3KUNLIK MALUMOT MAVJUD EMAS\nILTIMOS BUGUNGI YOKI ERTANGI\nMALUMOTLARDAN FOYDALANIB TURING.JAMOAMIZ BU MUAMONI TEZ ORADA XAR QILADI\n'
    message += f'{"🙏iltimos".upper()} namoz vaqtlarini xar \n3⃣ 3 kunda almashtirib turing'
    await bot.send_message(msg.chat.id,message)