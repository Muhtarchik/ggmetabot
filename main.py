import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import os

# Читаем токен из переменных окружения Render
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан! Добавьте его в Environment Variables Render.")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Приветственное сообщение и кнопки
@dp.message(CommandStart())
async def start_handler(message: types.Message):
    text = "🎁 Привет! Это Virus Gift Bot — место, где можно ловить халяву!\nВыбери, что тебе интересно 👇"
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="🎁 Получить подарок", url="https://t.me/ССЫЛКА_НА_РУЛЕТКУ")],
        [types.InlineKeyboardButton(text="💫 Купить звёзды", url="https://t.me/ССЫЛКА_НА_ПОКУПКУ")],
        [types.InlineKeyboardButton(text="💵 Получить $5 бонус", url="https://t.me/ССЫЛКА_НА_РЕГИСТРАЦИЮ")],
        [types.InlineKeyboardButton(text="🧠 Подписаться на канал", url="https://t.me/virusmetg")]
    ])
    await message.answer(text, reply_markup=keyboard)

# Запуск бота
async def main():
    print("🤖 Бот запущен 24/7 на Render!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
