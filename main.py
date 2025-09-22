from telegram import Update
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters, CallbackContext

BOT_TOKEN = "7741854679:AAHNSANHs5GhlbuVm_hnOT90-Vrb1gJP1Vs"
ADMIN_CHAT_ID = 7832676475  # твой Telegram id

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Отправь мне анонимное сообщение — я передам его админу ✅")

def handle_text(update: Update, context: CallbackContext):
    text = update.message.text
    context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=f"🔒 Анонимное сообщение:\n\n{text}")
    update.message.reply_text("Сообщение отправлено анонимно ✅")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    print("Бот запущен!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
