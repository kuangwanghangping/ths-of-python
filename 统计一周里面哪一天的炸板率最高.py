import time

import tushare as ts
from crazy import *
import pandas as pd
dataframe_completely_display ()
pro = ts.pro_api()
from datetime import datetime
df = pro.ths_daily(ts_code='883910.TI', start_date='20211127', end_date='20231122', fields='ts_code,trade_date,open,close,high,low,pct_change')


# 将字符串日期转换为datetime对象
df['date'] = pd.to_datetime(df['trade_date'])
# 使用apply函数获取星期几并存入新列
df['weekday'] = df['date'].apply(lambda x: x.day_name())
print(df)
trade_date = df['trade_date'].tolist()
print(trade_date)
Monday_zhang_zha = []
Tuesday_zhang_zha = []
Wednesday_zhang_zha = []
Thursday_zhang_zha = []
Friday_zhang_zha = []
Monday_zha = []
Tuesday_zha = []
Wednesday_zha = []
Thursday_zha = []
Friday_zha = []
for date in trade_date:
    pro = ts.pro_api()
    df_zha = pro.limit_list_d(trade_date=date, limit_type='Z',
                          fields='ts_code,trade_date,industry,name,close,pct_chg,open_times,up_stat,limit_times')

    df_zha['date'] = pd.to_datetime(df_zha['trade_date'])
    df_zha['weekday'] = df_zha['date'].apply(lambda x: x.day_name())
    #print(df_zha)
    print(date)
    if not df_zha.empty:
        if df_zha['weekday'].tolist()[-1] == 'Friday':
            Friday_zha.append(len(df_zha['weekday'].tolist()))
            Friday_zhang_zha.append(len(df_zha['weekday'].tolist()))
        if df_zha['weekday'].tolist()[-1] == 'Thursday':
            Thursday_zha.append(len(df_zha['weekday'].tolist()))
            Thursday_zhang_zha.append(len(df_zha['weekday'].tolist()))
        if df_zha['weekday'].tolist()[-1] == 'Wednesday':
            Wednesday_zha.append(len(df_zha['weekday'].tolist()))
            Wednesday_zhang_zha.append(len(df_zha['weekday'].tolist()))
        if df_zha['weekday'].tolist()[-1] == 'Tuesday':
            Tuesday_zha.append(len(df_zha['weekday'].tolist()))
            Tuesday_zhang_zha.append(len(df_zha['weekday'].tolist()))
        if df_zha['weekday'].tolist()[-1] == 'Monday':
            Monday_zha.append(len(df_zha['weekday'].tolist()))
            Monday_zhang_zha.append(len(df_zha['weekday'].tolist()))
    time.sleep(2)
for date in trade_date:
    pro = ts.pro_api()
    df_zhang = pro.limit_list_d(trade_date=date, limit_type='U',
                          fields='ts_code,trade_date,industry,name,close,pct_chg,open_times,up_stat,limit_times')
    df_zhang['date'] = pd.to_datetime(df_zhang['trade_date'])
    df_zhang['weekday'] = df_zhang['date'].apply(lambda x: x.day_name())
    if not df_zhang.empty:
        if df_zhang['weekday'].tolist()[-1] == 'Friday':
            Friday_zhang_zha.append(len(df_zhang['weekday'].tolist()))
        if df_zhang['weekday'].tolist()[-1] == 'Thursday':
            Thursday_zhang_zha.append(len(df_zhang['weekday'].tolist()))
        if df_zhang['weekday'].tolist()[-1] == 'Wednesday':
            Wednesday_zhang_zha.append(len(df_zhang['weekday'].tolist()))
        if df_zhang['weekday'].tolist()[-1] == 'Tuesday':
            Tuesday_zhang_zha.append(len(df_zhang['weekday'].tolist()))
        if df_zhang['weekday'].tolist()[-1] == 'Monday':
            Monday_zhang_zha.append(len(df_zhang['weekday'].tolist()))
    time.sleep(2)
    print(date)


print('星期五' + str(sum(Friday_zha)/sum(Friday_zhang_zha)*100))
print('星期四' + str(sum(Thursday_zha)/sum(Thursday_zhang_zha)*100))
print('星期三' +str(sum(Wednesday_zha)/sum(Wednesday_zhang_zha)*100))
print('星期二' + str(sum(Tuesday_zha)/sum(Tuesday_zhang_zha)*100))
print('星期一' + str(sum(Monday_zha)/sum(Monday_zhang_zha)*100))
