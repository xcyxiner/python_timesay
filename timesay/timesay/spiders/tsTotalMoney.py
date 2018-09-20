#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy
import json
import numpy as np
from timesay.items import TimesayItem
from timesay.items import TimesayUrlItem
from timesay.items import TimesayWinItem
class tsMoneySpider(scrapy.Spider):
    name="tsTotalMoney"
    url_pre="http://timesay.me/bet2.php?p="
    start_urls=[]
    i=1
    while i<25:
        start_urls.append(url_pre+str(i))
        i=i+1
    def parse(self,response):
        for moneyval in response.xpath("//div[@class='left720']//em//text()"):
            item = TimesayItem()
            item["money"]=moneyval.extract()
            yield item
class tsUrlSpider(scrapy.Spider):
    name="timesayUrl"
    url_pre="http://timesay.me/bet2.php?p="
    start_urls=[]
    i=1
    while i<25:
        start_urls.append(url_pre+str(i))
        i=i+1
    def parse(self,response):
        for urlval in response.xpath("//div[@class='left720']//a[contains(@href,'betid')]/@href"):
            item = TimesayUrlItem()
            item["url"]=urlval.extract()
            yield item 
class tsWinSpider(scrapy.Spider):
    name="timesayWin"
    url_pre="http://timesay.me/"
    start_urls=[]
    with open('url.json') as file_object:
        contents = file_object.read()
    urlJson = json.loads(contents)
    urlList=[]
    for urlInfo in urlJson:
        tmpUrl= url_pre+urlInfo["url"]
        urlList.append(tmpUrl)
    start_urls=np.unique(urlList)
    print start_urls
    def parse(self,response):
        sel=response.xpath("//div[@class='bet-details']//form//tr//td[@bgcolor='#eeeeee']")
        i=1
        while i <len(sel)+1:
            tmpspan=response.xpath("(//div[@class='bet-details']//form//tr//td[@bgcolor='#eeeeee'])["+str(i)+"]/span/text()").extract()
            if len(tmpspan)>0:
                if tmpspan[0]==u'\u83b7\u80dc\uff01':
                    tmpPercentage=response.xpath("((((//div[@class='bet-details']//form//tr)//td)["+str(i+1)+"]//div)[2]/text())").extract()
                    tmpPercentageArray=tmpPercentage[0].split('%')
                    item = TimesayWinItem()
                    item["winPercentage"]=tmpPercentageArray[0]
                    moneyInfo=response.xpath("(//div[@class='bet-details']//em[@class='smallprice'])/text()").extract()
                    item["money"]=moneyInfo[0]
                    print item
                    yield item
            i+=1