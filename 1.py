import numpy as np
import matplotlib.pyplot as plt
 
labels = 'A', 'B', 'C', 'D'
fracs = [15, 30.55, 44.44, 10]
explode = [0, 0.1, 0, 0]
plt.axes(aspect=1) 
plt.pie(x=fracs, labels=labels, explode=explode,autopct='%3.1f %%',shadow=True, labeldistance=1.1, startangle = 90,pctdistance = 0.6)
plt.show()