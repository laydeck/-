from sovet import sovets
import os
import random
import telebot 
token='token'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_bye(message):
    bot.reply_to(message, "Привет! Тут я расскажу про загрязнение окружающей среды и дам тебе советов которые помогут сохранить природу.Напаиши /Help чтоюы увидеть список команд")
    
@bot.message_handler(commands=['Help'])
def send_bye(message):
    bot.reply_to(message,
                 '''1./sovet:эта команда даст тебе рандомный совет что надо делать с твоим мусором \n 
2./itog:эта команда пришлет тебе фото последствий не правильного обращения с мусором
3./bye:ты прощаещся с ботом
                ''')
    
@bot.message_handler(commands=['sovet'])
def send_welcome(message):
    bot.reply_to(message, random.choice(sovets))
    
@bot.message_handler(commands=['itog'])
def send_mem(message):
    image_name=random.choice(os.listdir('images_sreda'))

    with open(f'images_sreda/{image_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "пока")
    
#последняя функция
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
print('бот запущен') 
bot.polling()
