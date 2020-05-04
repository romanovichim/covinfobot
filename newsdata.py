#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def news(xml_news_url):

    parse_xml_url = urlopen(xml_news_url)
    xml_page = parse_xml_url.read()
    parse_xml_url.close()

    soup_page = BeautifulSoup(xml_page, "xml")
    news_list = soup_page.findAll("item")
    #Искомое
    matches = ["коронавирус", "ОРВИ","врач"]
    #Сюда соберем новости
    newsform=[]
    for getfeed in news_list:
        if any(x in getfeed.title.text for x in matches):
            a=[]
            titlenou = getfeed.title.text.replace(u'\xa0', u' ')
            titlenol = getfeed.link.text.replace(u'\xa0', u' ')
            a.append(titlenou)
            a.append(titlenol)
            newsform.append(a)
            #print("\n")
            #print('\033[1;33m %s \033[1;m' %getfeed.title.text)
            #print('\033[1;32m %s \033[1;m' %getfeed.link.text)
            #print('\033[1;35m %s \033[1;m' %getfeed.pubDate.text)
            #print("\n")

    return newsform


