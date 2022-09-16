from flask import Flask
from flask import request
from flask import Response
#from chatty import chatbot
import requests
import telebot.credentials as keys
from telegram.ext import *
import responses as R

app = Flask(__name__)

print("Bot is running")


def start_command(update, context):
    update.message.reply_text("Type something random to get started😁")

def help_command(update, context):
    update.message.reply_text("I cannot help you")

def handle_message(update, context):
    text=str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater=Updater(keys.bot_token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help", start_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

if __name__ == '__main__':
    app.run(debug=True)


