#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from fuzzywuzzy import fuzz
import pymorphy2

#создание объекта морфологического анализатора
morph = pymorphy2.MorphAnalyzer()
#загрузка базы знаний
with open("faq.json") as json_file:
    faq = json.load(json_file)


def classify_question(text):
    #лемматизация текста юзера
    text = ' '.join(morph.parse(word)[0].normal_form for word in text.split())
    questions = list(faq.keys())
    scores = list()
    #цикл по всем вопросам из базы знаний
    for question in questions:
        #лемматизация вопроса из базы знаний
        norm_question = ' '.join(morph.parse(word)[0].normal_form for word in question.split())
        #сравнение вопроса юзера и вопроса из базы знаний
        scores.append(fuzz.token_sort_ratio(norm_question.lower(), text.lower()))
	#получение ответа

	
    if(max(scores)> 26):
        answer = faq[questions[scores.index(max(scores))]]
    else:
        answer="Хм, этого я пока не знаю, но я запомнил и в следущий раз точно отвечу"
    
    return answer
