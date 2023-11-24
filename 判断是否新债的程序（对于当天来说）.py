import tushare as ts
import pandas as pd
from datetime import datetime
pro = ts.pro_api()
#获取可转债发行数据
df = pro.ths_daily(ts_code='883910.TI', start_date='20231101', end_date='20231121', fields='ts_code,trade_date,open,close,high,low,pct_change')
# 将字符串日期转换为datetime对象
data_list  = df['trade_date'].tolist()   #获得这段时间可以交易的时间的列表
print(data_list)
df = pro.cb_basic(fields="ts_code,bond_short_name,stk_code,stk_short_name,list_date,delist_date")
print(df)#这个是转债的dataframe
for i in range(len(data_list)):
    if i+4<len(data_list):
        five_day = []#['20231121', '20231120', '20231117', '20231116', '20231115']
        five_day.append(data_list[i])
        five_day.append(data_list[i + 1])
        five_day.append(data_list[i + 2])
        five_day.append(data_list[i + 3])
        five_day.append(data_list[i + 4])
        formatted_dates = [datetime.strptime(date, '%Y%m%d').strftime('%Y-%m-%d') for date in five_day]
        #print(formatted_dates)
#转化为这个形式['2023-11-21', '2023-11-20', '2023-11-17', '2023-11-16', '2023-11-15']
        selected_ts_code=[]#[['113678.SH'], ['123229.SZ'], ['127097.SZ'], [], ['127096.SZ']]
        for i in formatted_dates:
            selected_ts_code.append(df[(df['list_date'] == i)]['ts_code'].tolist())
            small_lists = [item for sublist in selected_ts_code for item in sublist]
            #取出大列表里面的小列表['123228.SZ', '127094.SZ', '123226.SZ', '127093.SZ']
            print(small_lists)

#       ts_code  ann_date  issue_size
#0    123232.SZ  20231123      2.0251
#1    127098.SZ  20231122      4.7000
#2    113680.SH  20231113      3.0000
#q取出这个dataframe列表里面'ann_date']==220231123和22的转债
#selected_ts_code = df[(df['ann_date'] == '20231123') | (df['ann_date'] == '20231122')]['ts_code'].tolist()
#['123232.SZ', '127098.SZ']











#去除列表里面的小列表

#['113678.SH', '123229.SZ', '127097.SZ', '127096.SZ']