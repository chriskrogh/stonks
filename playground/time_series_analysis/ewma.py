import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

airline = pd.read_csv('airline_passengers.csv', index_col='Month')
airline.dropna(inplace=True)
airline.index = pd.to_datetime(airline.index)

# compute SMA
airline['6-month-SMA'] = airline['Thousands of Passengers'].rolling(
    window=6).mean()
airline['12-month-SMA'] = airline['Thousands of Passengers'].rolling(
    window=12).mean()

# compute EWMA
airline['12-month-EWMA'] = airline['Thousands of Passengers'].ewm(
    span=12).mean()
airline['6-month-EWMA'] = airline['Thousands of Passengers'].ewm(
    span=6).mean()

plt.plot(airline[['Thousands of Passengers', '12-month-SMA', '12-month-EWMA']])
plt.show()
