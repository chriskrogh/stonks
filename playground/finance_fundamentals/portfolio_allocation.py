import pandas as pd
import matplotlib.pyplot as plt
import quandl

# get data over 5 years
start = pd.to_datetime('2012-01-01')
end = pd.to_datetime('2017-01-01')

aapl = quandl.get('WIKI/AAPL.11', start_date=start, end_date=end)
csco = quandl.get('WIKI/CSCO.11', start_date=start, end_date=end)
ibm = quandl.get('WIKI/IBM.11', start_date=start, end_date=end)
amzn = quandl.get('WIKI/AMZN.11', start_date=start, end_date=end)

# normed return = close price / initial close price
for stock_df in (aapl, csco, ibm, amzn):
    stock_df['Normed Return'] = stock_df['Adj. Close'] / \
        stock_df.iloc[0]['Adj. Close']

# allocate investments based on ratio
for stock_df, allo in zip((aapl, csco, ibm, amzn), [0.3, 0.2, 0.4, 0.1]):
    stock_df['Allocation'] = stock_df['Normed Return'] * allo
    stock_df['Position Values'] = stock_df['Allocation'] * 1000000

all_pos_values = [aapl['Position Values'], csco['Position Values'],
                  ibm['Position Values'], amzn['Position Values']]

portfolio_val = pd.concat(all_pos_values, axis=1)
portfolio_val.columns = ['AAPL', 'CSCO', 'IBM', 'AMZN']
portfolio_val['Total'] = portfolio_val.sum(axis=1)

# daily return = percentage change between current and prior total
portfolio_val['Daily Return'] = portfolio_val['Total'].pct_change(1)

# calculate Sharpe ratio and Annual Sharpe ratio
SR = portfolio_val['Daily Return'].mean() / portfolio_val['Daily Return'].std()

ASR = (252**0.5) * SR

print(portfolio_val.head())
