from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = 8802958009:AAEM4Cxs5OxpXC8zGB7W_hpZ1yIgM1-T6iY

async def start(update, context):
    await update.message.reply_text("Halo! Bot saya sudah berjalan!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot berjalan!")
    app.run_polling()
