from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

airline = pd.read_csv('airline_passengers.csv', index_col='Month')
airline.dropna(inplace=True)
airline.index = pd.to_datetime(airline.index)


result = seasonal_decompose(
    airline['Thousands of Passengers'], model='multiplicative')

plt.plot(result)
plt.show()

# plt.plot(airline)
# plt.show()
