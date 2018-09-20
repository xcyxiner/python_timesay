import json
import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd
import csv
with open('timesay/url.json') as file_object:
    contents = file_object.read()
urlJson = json.loads(contents)
urlList=[]
url_pre="http://timesay.me/"
for urlInfo in urlJson:
    tmpUrl= url_pre+urlInfo["url"]
    urlList.append(tmpUrl)
newList=np.unique(urlList)
print len(urlList)
print len(newList)
print newList