import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiohttp import web

# Получаем токен и URL из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
RENDER_EXTERNAL_URL = os.getenv("RENDER_EXTERNAL_URL")

if not BOT_TOKEN:
    raise RuntimeError("❌ BOT_TOKEN не задан! Добавь его в Environment Variables Render.")
if not RENDER_EXTERNAL_URL:
    raise RuntimeError("❌ RENDER_EXTERNAL_URL не задан! Добавь его в Environment Variables Render.")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()  # В 3.22 бот не передается в конструктор

# === Команда /start ===
@dp.message(CommandStart())
async def start_handler(message: types.Message):
    text = "🎁 Привет! Это Virus Gift Bot — выбирай, что тебе интересно 👇"
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="🎁 Получить подарок", url="https://t.me/virus_play_bot/app?startapp=roulette_inviteCodesmKkOJLS3JDvHhYM")],
        [types.InlineKeyboardButton(text="💫 Купить звёзды", url="https://split.tg/?ref=UQAENEC9lNreXR8K35LgVzEKK3zAL4-8Dq5d-0rqFMZuDmFC")],
        [types.InlineKeyboardButton(text="💵 Получить скин за $5 (промо BETME)", url="https://plg.bet/ru/affiliates")],
        [types.InlineKeyboardButton(text="🧠 Подписаться на канал", url="https://t.me/virusmetg")],
        [types.InlineKeyboardButton(text="🎮 Маркетплейс tg подарков", url="https://t.me/portals/market?startapp=4vp0jk")],
        [types.InlineKeyboardButton(text="🎰 Рулетка tg подарков", url="https://t.me/rollsgame_bot/app?startapp=ref_jeBivgoYMO")],
    ])
    await message.answer(text, reply_markup=keyboard)

# === Webhook setup ===
async def on_startup(app):
    webhook_url = f"{RENDER_EXTERNAL_URL}/webhook"
    await bot.set_webhook(webhook_url)
    print(f"✅ Webhook установлен: {webhook_url}")

async def on_shutdown(app):
    await bot.delete_webhook()
    await bot.session.close()
    print("🛑 Webhook удалён и бот остановлен.")

# === Обработка webhook ===
async def handle_webhook(request):
    data = await request.json()
    update = types.Update(**data)
    await dp.feed_update(bot, update)
    return web.Response()

# === Запуск aiohttp сервера ===
app = web.Application()
app.router.add_post("/webhook", handle_webhook)
app.on_startup.append(on_startup)
app.on_shutdown.append(on_shutdown)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    web.run_app(app, host="0.0.0.0", port=port)
