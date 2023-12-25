import tushare as ts
from crazy import *
import pandas as pd
dataframe_completely_display ()
pro = ts.pro_api()
from datetime import datetime
df = pro.ths_daily(ts_code='883910.TI', start_date='20181101', end_date='20231118', fields='ts_code,trade_date,open,close,high,low,pct_change')
# 将字符串日期转换为datetime对象
df['date'] = pd.to_datetime(df['trade_date'])
# 使用apply函数获取星期几并存入新列
df['month'] = df['date'].apply(lambda x: x.month)
print(df)