from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
TOKEN = "XXX-YOUR-TOKEN"

def start(bot, update):
  update.message.reply_text("Bot sobre ciclismo creado por Jonatan Navarrete")

def convert_uppercase(bot, update):
  update.message.reply_text(update.message.text.upper())

def main():
  # Create Updater object and attach dispatcher to it
  updater = Updater(TOKEN)
  dispatcher = updater.dispatcher
  print("Bot started")

  # Add command handler to dispatcher
  start_handler = CommandHandler('start',start)
  upper_case = MessageHandler(Filters.text, convert_uppercase)
  dispatcher.add_handler(start_handler)
  dispatcher.add_handler(upper_case)

  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()

if __name__ == '__main__':
  main()
