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
df['weekday'] = df['date'].apply(lambda x: x.day_name())
df['chajia'] = df['high']  - df['low'].shift(-1)
print(df)
df.dropna(subset=['chajia'], inplace=True)
# 打印结果
print(df)
grouped = df.groupby('weekday')
list = []
list1 = []
# 遍历每个分组并打印结果
for group_name, group_df in grouped:
    print(f"Data for {group_name}:")
    group_df_sl = group_df.shape
    print(group_df_sl)

    sum_of_column_A = group_df['pct_change'].sum()
    print(sum_of_column_A)
    aver_zhangfu = sum_of_column_A/ group_df_sl[0]
    print(group_name + str(aver_zhangfu))
    print(group_df)
    print("\n")
    sum_of_column_B = group_df['chajia'].sum()
    aver_zhangfu_2 = sum_of_column_B/ group_df_sl[0]
    list.append(group_name + str(aver_zhangfu))
    list1.append(group_name + str(aver_zhangfu_2))
print(list)
print(list1)































