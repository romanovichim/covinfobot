#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bingo_generator import Bingo
import random


entries = [
    'Спасибо, что остаетесь дома!',
    'У карантина есть неоспоримый плюс...',
    'Коронавирусный пост на три экрана от человека, на которого ты забыл что подписан',
    'В рабочем чате присылают новость про вред 5G-сетей',
    'Для тех, кто дома...',
    'В чате обсуждают рабочие вопросы в 23:00',
    'Реклама курсов по извлечению прибыли из кризиса',
    'Емейл от интернет магазина с описанием коронавирусных мер на складе',
    'Кофейня в инстаграме зовет всех выходить на улицу и пить кофе',
    'Подводка статьи начинается с Самое время...',
    'Мы работаем, чтобы Вы сидели дома',
    'Шутки про прогулки на балконе',
    'Знаменитость вещает про чипирование',
    'Бабушка по телефону просит тебя беречь себя',
    'Бабушка по телефону сообщает, что ходит в Пятерочку каждый день',
    'Очередной пакет неотложных мер',
    'Подпишите онлайн петицию',
    'Мем про туалетную бумагу в рабочем чате',
    'Промокод: COVID19',
    'ВЫ МЕНЯ СЛЫШИТЕ? в Zoom',
    'Чья-то собака лает в Zoom',
    'Кто-то рассказывает, что он интроверт и ему норм',
    'Один и тот же мем присылают дважды за день',
    'Посмотрев на улицу, завидуешь людям с собакой',
    'Шутка про 2020 directed by by Robert b Weide',
    'Новость про Ухань'
    ]

def generatebingo():
    #lets make shuffle
    random.shuffle(entries)
    bing = Bingo.make_bingo_from_scratch(entries=entries, title='Cгенерируй свое бинго ICQ: @covid_info_bot')

    return r"bingo.jpg"


