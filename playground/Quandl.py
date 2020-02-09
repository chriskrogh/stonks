import quandl
import matplotlib.pyplot as plt

mydata = quandl.get('EIA/PET_RWTC_D')
print(mydata.head())
