import os
import requests
from pyrogram import Client, filters

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("7934341869:AAHgU6sVxXsmNGMgVgMqYo6tl61NB-Kpt-k")

TIKCDN_API = "https://api.tikcdn.io/v1/video"

app = Client("tiktok_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.text & filters.private)
async def download_tiktok(client, message):
    url = message.text.strip()
    if "tiktok.com" not in url:
        await message.reply("Пожалуйста, пришли ссылку на TikTok 🎯")
        return

    await message.reply("🔄 Скачиваю...")

    try:
        response = requests.get(TIKCDN_API, params={"url": url})
        data = response.json()

        if data["status"] != "ok":
            await message.reply("⚠️ Видео не удалось скачать.")
            return

        video_url = data["data"]["play"]
        await message.reply_video(video_url, caption="✅ Готово, без водяного знака")
    except Exception as e:
        await message.reply(f"Ошибка: {e}")

app.run()
