import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("❌ BOT_TOKEN не задан! Добавь его в Environment Variables Render.")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(CommandStart())
async def start_handler(message: types.Message):
    text = (
        "🎁 Привет! Это Virus Gift Bot — выбирай, что тебе интересно 👇"
    )
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="🎁 Получить подарок", url="https://t.me/virus_play_bot/app?startapp=roulette_inviteCodesmKkOJLS3JDvHhYM")],
        [types.InlineKeyboardButton(text="💫 Купить звёзды", url="https://split.tg/?ref=UQAENEC9lNreXR8K35LgVzEKK3zAL4-8Dq5d-0rqFMZuDmFC")],
        [types.InlineKeyboardButton(text="💵 Получить скин за $5 (промо BETME)", url="https://plg.bet/ru/affiliates")],
        [types.InlineKeyboardButton(text="🧠 Подписаться на канал", url="https://t.me/virusmetg")],
        [types.InlineKeyboardButton(text="🎮 Маркетплейс tg подарков", url="https://t.me/portals/market?startapp=4vp0jk")],
        [types.InlineKeyboardButton(text="🎰 Рулетка tg подарков", url="https://t.me/rollsgame_bot/app?startapp=ref_jeBivgoYMO")],
    ])
    await message.answer(text, reply_markup=keyboard)

# Запуск Long Polling
async def main():
    print("✅ Бот запущен на Long Polling, работает 24/7!")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        print("🛑 Бот остановлен.")

if __name__ == "__main__":
    asyncio.run(main())
