from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

TOKEN = "8759624574:AAFUIt29xnnUJZYqNGsC1FPgcV_Fz1KPMn8"

def menu():
    keyboard = [
        [InlineKeyboardButton("▶️ Start", callback_data="start")],
        [InlineKeyboardButton("⏹ Stop", callback_data="stop")],
        [InlineKeyboardButton("📊 Status", callback_data="status")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update, context):
    await update.message.reply_text(
        "Bot Control Panel",
        reply_markup=menu()
    )

async def button(update, context):
    query = update.callback_query
    await query.answer()

    if query.data == "start":
        await query.edit_message_text("Worker started")

    if query.data == "stop":
        await query.edit_message_text("Worker stopped")

    if query.data == "status":
        await query.edit_message_text("Bot running normally")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("Bot running...")

app.run_polling()