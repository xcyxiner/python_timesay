import json
import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd
import csv
with open('timesay/items.json') as file_object:
    contents = file_object.read()
totalMoneyJson = json.loads(contents)
totalMoney=0
totalMoneyList=[]
for tmpMoneyInfo in totalMoneyJson:
    tmpMoney= float(tmpMoneyInfo["money"])
    totalMoneyList.append(tmpMoney)
    totalMoney+=tmpMoney
totalMoneyResult=sum(totalMoneyList)
# print max(totalMoneyList)
# print min(totalMoneyList)
# print np.mean(totalMoneyList)
# print np.sort(totalMoneyList)
print 'sum  '+str(totalMoneyResult)
print 'get  '+str(totalMoneyResult*0.01)
df=pd.read_json('timesay/money.json')
printResult= df.describe()
print printResult
x= range(0,len(totalMoneyList))
y=totalMoneyList
plt.plot(x,y,label="hello",color='r',marker='o',markerfacecolor='blue')
plt.show()
