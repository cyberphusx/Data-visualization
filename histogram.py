import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


#histogram

ages = np.random.normal(30,2.5,1000)

plt.hist(ages,bins=20,cumulative=True)
plt.show()