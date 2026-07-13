from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import os

SONGS = [
    ("505", "Arctic Monkeys", "https://youtu.be/qU9mHegkTc4"),
    ("Space Song", "Beach House", "https://youtu.be/RBtlPT23PTM"),
    ("The Chain", "Fleetwood Mac", "https://youtu.be/JDG2m5hN1vo"),
    ("After Dark", "Mr.Kitty", "https://youtu.be/sVx1mJDeUjY"),
    ("Sweater Weather", "The Neighbourhood", "https://youtu.be/GCdwKhTtNNw"),
    ("Mary on a Cross", "Ghost", "https://youtu.be/k5mX3NkA7jM"),
    ("Odoriko", "Vaundy", "https://youtu.be/7HgJIAUtICU"),
    ("Apocalypse", "Cigarettes After Sex", "https://youtu.be/sElE_BfQ67s"),
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 سلام!\n"
        "برای دریافت یک آهنگ رندوم دستور /random را بفرست."
    )

async def random_song(update: Update, context: ContextTypes.DEFAULT_TYPE):
    song = random.choice(SONGS)
    await update.message.reply_text(
        f"🎵 {song[0]}\n"
        f"👤 {song[1]}\n\n"
        f"▶️ {song[2]}"
    )

app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("random", random_song))

app.run_polling()