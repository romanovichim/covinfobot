#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from covid import Covid
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def covidnow():
    #Строка для сбора данных
    msgtoday="у меня какой-то сбой, починю - расскажу"
    covid = Covid(source="worldometers")
    russia_cases = covid.get_status_by_country_name("russia")
    #print(russia_cases)
    #print(russia_cases['confirmed'])
    #print(russia_cases['new_cases'])
    d1 = datetime.strptime("24.03.2020", "%d.%m.%Y")
    today = datetime.now()
    deltad = (today-d1).days
    q = (russia_cases['confirmed']/deltad)
    growth="Рост"
    if(q > russia_cases['new_cases']):
        growth = "Спад"

    msgtoday = "Главные цифры на сегодня:\n"+"Заражения: " + str(russia_cases['confirmed']) + "\n" + "За сутки: " +str(russia_cases['new_cases']) + "\n" + "Тенденция: " + growth

    return msgtoday
