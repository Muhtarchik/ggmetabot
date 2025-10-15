import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiohttp import web

# Токен из Render Environment Variables
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан! Добавьте его в Environment Variables Render.")

# Получаем URL Render (он появится после деплоя)
RENDER_EXTERNAL_URL = os.environ.get("RENDER_EXTERNAL_URL")
if not RENDER_EXTERNAL_URL:
    raise RuntimeError("RENDER_EXTERNAL_URL не задан! Добавьте переменную окружения.")

WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
WEBHOOK_URL = f"{RENDER_EXTERNAL_URL}{WEBHOOK_PATH}"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Команда /start
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

# ---------- AIOHTTP SERVER ----------
async def handle(request):
    update = await request.json()
    await dp.feed_update(bot, update)
    return web.Response()

async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)
    print(f"✅ Webhook установлен: {WEBHOOK_URL}")

async def on_shutdown(app):
    await bot.delete_webhook()
    await bot.session.close()
    print("🛑 Webhook удалён")

def main():
    app = web.Application()
    app.router.add_post(WEBHOOK_PATH, handle)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    web.run_app(app, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

if __name__ == "__main__":
    main()
