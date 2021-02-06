import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Logic
data = pd.read_csv("data/data.csv")

def smallest_difference(array):
    # Code a function that takes an array and returns the smallest
    # absolute difference between two elements of this array
    # Please note that the array can be large and that the more
    # computationally efficient the better
    array.sort()
    n = len(array)
    l=[]
    for i in range(1,n):
        absolute_difference = array[i]-array[i-1]
        if absolute_difference == 0:
            return 0
        else:
            l.append(absolute_difference)
    return min(l)

# Finance and DataFrame manipulation


def macd(prices, window_short=12, window_long=26):
    # Code a function that takes a DataFrame named prices and 
    # returns it's MACD (Moving Average Convergence Difference) as
    # a DataFrame with same shape
    # Assume simple moving average rather than exponential moving average
    # The expected output is in the output.csv file
    return  prices["SX5T Index"].rolling(window_short).mean() - prices["SX5T Index"].rolling(window_long).mean()


def sortino_ratio(prices):
    # Code a function that takes a DataFrame named prices and
    # returns the Sortino ratio for each column
    # Assume risk-free rate = 0
    # On the given test set, it should yield 0.05457


    yield_portfolio = - data["SX5T Index"].diff(periods=-1) / data["SX5T Index"]
    portofolio_mean_return = yield_portfolio[:-1].mean()
    yield_portfolio = yield_portfolio.reset_index()
    deviation_downside_returns = yield_portfolio.loc[yield_portfolio["SX5T Index"]<0][:-1].std()

    return yield_portfolio/deviation_downside_returns


def expected_shortfall(prices, level=0.95):
    # Code a function that takes a DataFrame named prices and
    # returns the expected shortfall at a given level
    # On the given test set, it should yield -0.03468
    yield_portfolio = - prices["SX5T Index"].diff(periods=-1) / prices["SX5T Index"]
    value_at_risk = yield_portfolio.quantile(1-0.95 ,interpolation='higher')    
    return yield_portfolio.dropna()[yield_portfolio.lt(value_at_risk)].mean()


# Plot 


def visualize(prices, path):
    # Code a function that takes a DataFrame named prices and
    # saves the plot to the given path
    prices.plot()
    plt.xlabel('Dates')
    plt.ylabel('Prices')
    plt.savefig(path)
    return None
