import numpy as np
import pandas as pd
from matplotlib import pyplot as plt





x_data = np.random.random(50)*100
y_data = np.random.random(50)*100


print("x:",x_data,"y:", y_data)
#scatter_plt = plt.scatter(x_data,y_data,c='grey',linewidths=2,marker='*')
#scatter_plt.legend_elements("X data")


years = [2006 + x for x in range(16)]
weight = [30,90,39,59,19, 45,80,100,29,67,70,60,99,60,100,76]

plt.plot(years,weight,lw=2,linestyle='--')
plt.show();