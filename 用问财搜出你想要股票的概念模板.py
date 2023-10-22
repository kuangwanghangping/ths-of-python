now = {}
import numpy as np
array = np.array
yese = {'128111.SZ': 359.99, '128026.SZ':100}
nowpr = {'128111.SZ': array([  0.   ,   0.   , 359.895, 359.699]), '128026.SZ': array([  0.   ,   0.   ,   0.   , 107.525])}
for i , ii in nowpr.items():
    now[i] = ii[-1]
print(now)

def today_growth(yest_price, now_price):
    today_growth1 = {}
    for i, price in yest_price.items():
        growth = (now_price[i] - price) / price * 100
        today_growth1[i] = growth
    return today_growth1
print(today_growth(yese,now))
