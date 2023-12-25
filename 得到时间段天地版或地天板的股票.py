import time

import pywencai
import tushare as ts
pro = ts.pro_api()
df = pro.ths_daily(ts_code='883910.TI', start_date='20221224', end_date='20231224', fields='ts_code,trade_date,open,close,high,low,pct_change')
date_list = df['trade_date'].tolist()
dict1 = {}
for i in date_list:
    try:
        res = pywencai.get(query=f"{i}振幅大于18%，主板，{i}跌停", loop=True)
        dict1[i] = res['股票简称'].tolist()
        print(res)
        time.sleep(13)
    except:
        print("无")
        time.sleep(10)
print(dict1)