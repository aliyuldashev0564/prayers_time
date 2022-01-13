import aiohttp
import datetime
async def times(long, lat):
    month = datetime.datetime.today().month
    year = datetime.datetime.today().year
    async with aiohttp.ClientSession() as sesion:
        async with sesion.get(f'http://api.aladhan.com/v1/calendar?latitude={lat}&longitude={long}&monthod=1&month={month}&year={year}') as res:
            return await res.json()