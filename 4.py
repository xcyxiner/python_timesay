import json
import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd
import csv
with open('timesay/win.json') as file_object:
    contents = file_object.read()
totalMoneyJson = json.loads(contents)
totalMoney=0
totalMoneyList=[]
for tmpMoneyInfo in totalMoneyJson:
    tmpMoney= float(tmpMoneyInfo["money"][0])
    tmpPercentage= float(tmpMoneyInfo["winPercentage"])
    tmpNewMoney=tmpMoney*0.95*tmpPercentage*0.01
    # print tmpNewMoney
    totalMoneyList.append(tmpNewMoney)
totalMoneyResult=sum(totalMoneyList)
print max(totalMoneyList)
print min(totalMoneyList)
print np.mean(totalMoneyList)
# print np.sort(totalMoneyList)
print 'winsum  '+str(totalMoneyResult)
# df=pd.read_json('timesay/items.json')
# printResult= df.describe()
# print printResult
# x= range(0,len(totalMoneyList))
# y=totalMoneyList
# plt.plot(x,y,label="hello",color='r',marker='o',markerfacecolor='blue')
# plt.show()
