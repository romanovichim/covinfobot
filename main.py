#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import config 
import json
from bot.bot import Bot
from bot.handler import MessageHandler, BotButtonCommandHandler
from reply_generator import classify_question
import newsdata
import coviddata
import randommem
import makebingo
import pymongo
bot = Bot(token=config.TOKEN)




def message_cb(bot, event):
    # залогируем для аналитики
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient['hackdb']
    mycol = mydb["msg"]
    d = dict(who='user', text=event.text, idchat = event.from_chat, timest = event.timestamp)
    x = mycol.insert_one(d)
    #получение ответа
    #исключим команды
    if((event.text).startswith("/")):
        #обработаем команды
        if(event.text=="/news"):
            #НОВОСТИ
            bot.send_text(chat_id=event.from_chat, text = "Топ 3 новости про короновирус на данный момент:")
            #Циклом возьмем топ 5 новостей на текущий момент c mail.ru
            newslist=newsdata.news(config.NEWS_URL)
            for element in newslist[0:3]:    
                bot.send_text(chat_id=event.from_chat, text = element[0]+"\n"+element[1])
        elif(event.text=="/now"):
            #ТЕКУЩИЕ ЦИФРЫ ПО КОРОНЕ
            bot.send_text(chat_id=event.from_chat, text = "Посылаю запрос на сервер - 5 сек)")
            nowdata = coviddata.covidnow()
            bot.send_text(chat_id=event.from_chat, text = nowdata)
        elif(event.text=="/memes"):
            bot.send_text(chat_id=event.from_chat, text = "Рандомный мемчик")
            #Берем мемчик
            #bot.send_text(chat_id=event.from_chat, text = "https://sun1-93.userapi.com/c855036/v855036822/2262a6/FYrdVlTAw2k.jpg")
            #рандомный мемчик
            with open(randommem.randmem() , "rb") as file:
                bot.send_file(chat_id=event.from_chat, file=file)
        elif(event.text=="/bingo"):
            bot.send_text(chat_id=event.from_chat, text = "Gенерирую бинго:")
            #
            bot.send_text(chat_id=event.from_chat, text = "Делитесь с друзьями и отслеживате совпадения в течение дня!")
            with open(makebingo.generatebingo() , "rb") as file:
                bot.send_file(chat_id=event.from_chat, file=file)
        elif(event.text=="/family"):
            bot.send_text(chat_id=event.from_chat, text = "Самоизоляция удобное время увлекательного развития мозга. Присоединятесь и подключайте детей: https://bit.ly/2xtzbiu")
        elif(event.text=="/psy"):
            bot.send_text(chat_id=event.from_chat, text = "Для этого у нас есть отдельный бот-психолог.Пользуйтесь на здоровье. @psybot")
        elif(event.text=="/start"):
            bot.send_text(chat_id=event.from_chat, text = "Привет! \nЯ инфо бот.! \n\nЯ сделаю так, чтобы вы парили над информационным шумом \n я знаю текующую информацию о заражении. \nВсе мои команды доступны по команде /help.\nПопробуйте следующие запросы: \n-Как носить маску?\n/now \n/news \n\nЕсли вы хотите поговорить с психологом, переходите:  \n@psybot  \n")
        elif(event.text=="/help"):
            bot.send_text(chat_id=event.from_chat, text = "Вот что я умею")
        else:
            bot.send_text(chat_id=event.from_chat, text = "Я пока не знаю, такой команды, все команды можно узнать по команде /help")
    else:
        answer = classify_question(event.text)
        bot.send_text(chat_id=event.from_chat, text = answer)
        #bot.send_text(chat_id=event.from_chat, text=event.text)



bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
bot.start_polling()
bot.idle()
