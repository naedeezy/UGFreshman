from flask import Flask
from flask import request
from flask import Response
from chatty import chatbot
import requests
from telegram import bot

TOKEN = "5793746150:AAHSKgYN5WvgJmjzyTMipv3LLg954GnG5zU"
app = Flask(__name__)

#def get_bot_response():
#    userText = request.args.get('msg')
#    return str(chatbot.get_response(userText))

def parse_message(message):
    print("message-->", message)
    chat_id = message['message']['chat']['id']
    try:
        txt = message['message']['text']
    except:
        txt = "This is not text."
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id, txt

def sticker_message(message):
    print("message-->", message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['sticker']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id, txt


def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    r = requests.post(url, json=payload)
    return r

def tel_send_image(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': "https://raw.githubusercontent.com/fbsamples/original-coast-clothing/main/public/styles/male-work.jpg",
        'caption': "This is a sample image"
    }

    r = requests.post(url, json=payload)
    return r

def handling_sticker(message):
   sticker_id = message.file_id
   if sticker_id == '123456789':
      bot.send_message(message.chat.id, f'Something {sticker_id}')


def tel_send_audio(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendAudio'

    payload = {
        'chat_id': chat_id,
        "audio": "http://www.largesound.com/ashborytour/sound/brobob.mp3",

    }

    r = requests.post(url, json=payload)

    return r



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()

        chat_id, txt = parse_message(msg)
        reply = str(chatbot.get_response(txt))

        tel_send_message(chat_id, reply)
#        else:
#            tel_send_message(chat_id, 'from webhook')

#        if txt == "hi":
#            tel_send_message(chat_id, "Hello!!")
#        elif txt == "image":
#            tel_send_image(chat_id)
#        elif txt == "audio":
#            tel_send_audio(chat_id)
#
#        else:
#            tel_send_message(chat_id, 'from webhook')

        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"

#@app.route("/get")
#def get_bot_response():
#    userText = request.args.get('msg')
#    return str(chatbot.get_response(userText))

if __name__ == '__main__':
    app.run(debug=True)