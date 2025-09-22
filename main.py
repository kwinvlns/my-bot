# Требования: pip install aiogram==3.1.0
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardRemove
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer("Отправь мне анонимное сообщение — я пришлю его админу.", reply_markup=ReplyKeyboardRemove())

@dp.message()
async def handle_message(message: Message):
    # Формируем анонимное сообщение
    if message.text:
        await bot.send_message(chat_id=ADMIN_CHAT_ID, text=f"🔒 Анонимное сообщение:\n\n{message.text}")
        await message.answer("Сообщение отправлено анонимно ✅")
    elif message.photo:
        photo = message.photo[-1]
        await bot.send_photo(chat_id=ADMIN_CHAT_ID, photo=photo.file_id, caption=f"🔒 Анонимное фото:\n\n{message.caption or ''}")
        await message.answer("Фото отправлено анонимно ✅")
    elif message.document:
        doc = message.document
        await bot.send_document(chat_id=ADMIN_CHAT_ID, document=doc.file_id, caption=f"🔒 Анонимный файл:\n\n{message.caption or ''}")
        await message.answer("Файл отправлен анонимно ✅")
    else:
        await message.answer("Этот тип сообщений пока не поддерживается ❌")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
