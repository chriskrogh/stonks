import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_p = '../../data/'

aapl = pd.read_csv(data_p + 'AAPL_CLOSE.csv',
                   index_col='Date', parse_dates=True)
csco = pd.read_csv(data_p + 'CSCO_CLOSE.csv',
                   index_col='Date', parse_dates=True)
ibm = pd.read_csv(data_p + 'IBM_CLOSE.csv',
                  index_col='Date', parse_dates=True)
amzn = pd.read_csv(data_p + 'AMZN_CLOSE.csv',
                   index_col='Date', parse_dates=True)

stocks = pd.concat([aapl, csco, ibm, amzn], axis=1)
stocks.columns = ['aapl', 'csco', 'ibm', 'amzn']

log_returns = np.log(stocks / stocks.shift(1))

weights = np.array(np.random.randint(4))
weights = weights/np.sum(weights)
print(weights)

# print(stocks.head())

# plt.plot(stocks)
# plt.show()
