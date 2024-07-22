#comment

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5893227796:AAHj9t6W1epzcjmNCBn_4zpx0YuOIDAViLg").build()

app.add_handler(CommandHandler("hello", hello))
print("start_bot")
app.run_polling()
