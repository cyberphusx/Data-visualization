import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#pie chart are for independent categories
language_choice = ['c++','c','java','rust','python','go','c#','ruby','perl','dart']
language_value= [20 *(x+2) for x in range(len(language_choice))]
explodes = [0.1,0,0,0,0,0,0,0,0,0]
plt.pie(language_value,labels=language_choice,explode=explodes,autopct='%.2f%%',pctdistance=.7, startangle=45)
plt.show()

