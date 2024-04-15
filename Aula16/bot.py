from telegram.ext import *
import constans, responses

def start_command(update, context):
   update.message.reply_text(f"Olá {update.message.from_user['first_name']} Seja bem vindo ")
                               
def help_command(update, context):
   txt = str(update.message.reply_text("oi ou olá -> retorna uma saudação\n anual -> retorna informação"))

def handle_message(update, context):
   txt = str(update.message.text).lower()
   response = responses.sample_responses(txt)

   update.message.reply_text(response)

def error(update, context):
    print(f"Update: {update} caused error: {context.error}")

def main():
    update = Updater(constans.API_KEY, use_context = True)
    dp = Updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(filters.Text, handle_message))
    dp.add_error_handler(error)

    update.start_polling
    update.idle()

    main()




