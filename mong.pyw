import asyncio
import logging

import pyautogui
from aiogram.types import FSInputFile
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text

logging.basicConfig(level=logging.INFO)

# Bot assignment--------------------------------------------------------------------------------------------------------
bot = Bot(token=config.TOKEN)
dp = Dispatcher()


@dp.message(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("Бот готов работать. Для запроса введите любую цифру")


@dp.message(lambda message: message.text in "1234567890")
async def with_puree(message: types.Message):
    if message.from_user.id in config.user:
        path_for_save = "./tmp.jpg"
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(path_for_save)
        img = FSInputFile("./tmp.jpg")
        await message.answer_photo(photo=img)
        img.close()


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
