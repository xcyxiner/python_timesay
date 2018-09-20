cd timesay
#获取已结束的统计金额
#scrapy crawl tsTotalMoney -o money.json
#scrapy crawl timesayUrl -o url.json
#scrapy crawl timesayWin -o win.json
#获取已答题总金额
#response.xpath("//div[@class='left720']//em//text()").extract()
#获取每次答题详情
#response.xpath("//div[@class='left720']//a[contains(@href,'betid')]/@href").extract() 答题的URL地址
#获取获胜金额百分比
#response.xpath("(((//div[@class='bet-details']//form//tr)//td)[7]/span/text())").extract()   [u'\u83b7\u80dc\uff01'] 获胜条件
#response.xpath("((((//div[@class='bet-details']//form//tr)//td)[8]//div)[2]/text())").extract()  [u'1.02%\xa0']  比率