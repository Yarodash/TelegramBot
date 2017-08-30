import telebot
import TelegramToken
import Parsing

bot = telebot.TeleBot(TelegramToken.Token)

def SendMessage(message):
    print('Message to',userid.from_user.first_name,userid.from_user.last_name,message)
    bot.send_message(userid.chat.id,message)

def SendKeyboard(message):
    print('Message to',userid.from_user.first_name,userid.from_user.last_name,message)
    bot.send_message(userid.chat.id,message,reply_markup=user_markup)

global user_markup
user_markup = telebot.types.ReplyKeyboardMarkup()

@bot.message_handler(content_types=['text'])
def handler_text(user):
    print('--------')
    message = user.text
    print('Message from', user.from_user.first_name, user.from_user.last_name, message)

    global userid
    userid = user

    if message == '/start':
        SendMessage('/help to show available commands')

    if message == '/help':
        SendMessage('/help to show available commands')



bot.polling(none_stop=True, interval=0)