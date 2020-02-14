import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import statsmodels.api as sm

df = sm.datasets.macrodata.load_pandas().data
index = pd.Index(sm.tsa.datetools.dates_from_range('1959Q1', '2009Q3'))
df.index = index

# print(df.head())

plt.plot(df)
plt.show()
