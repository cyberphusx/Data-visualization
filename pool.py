import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
language_choice = ['c++','c','java','rust','python','go','c#','ruby','perl','dart']
language_value= [20 *x for x in range(len(language_choice))]

#draw a bar chart for categorical

plt.bar(language_choice,language_value,color='green',align='edge',width=0.7,edgecolor='#ad123434',lw=2)
plt.title('Most used Langauge') #chart title
plt.xlabel('Languge') #x Axis name
plt.ylabel('Vote Count') #y Axis name
plt.show()

