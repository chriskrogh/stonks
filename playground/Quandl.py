import quandl
import matplotlib.pyplot as plt

mydata = quandl.get('WIKI/AAPL')
print(mydata.head())
