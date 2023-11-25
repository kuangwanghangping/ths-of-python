import time

import tushare as ts
from crazy import *
import pandas as pd
dataframe_completely_display ()
pro = ts.pro_api()
from datetime import datetime
df = pro.ths_daily(ts_code='883910.TI', start_date='20221101', end_date='20231118', fields='ts_code,trade_date,open,close,high,low,pct_change')
date_list = df['trade_date'].tolist()
date_list = date_list[::-1]
print(date_list)
output_dfs = []  # 创建一个空列表来存储DataFrame
for i in range(len(date_list)):
    if i == 0 or i == len(date_list) -1 :
        continue
    else:
        df = pro.limit_list_d(trade_date=date_list[i], limit_type='U',
                              fields='ts_code,trade_date,industry,name,first_time,close,pct_chg,open_times,up_stat,limit_times')
        output_df = df[df['ts_code'].str.startswith('30') | df['ts_code'].str.startswith('688')]
        time.sleep(0.1)
        geyezhangfu = {}
        for stock in output_df['ts_code'].tolist():
            df1 = pro.query('daily', ts_code=stock, start_date=date_list[i+1], end_date=date_list[i+1])
            geyezhangfu[stock] = df1['open'].iloc[0]
        output_df_copy = output_df.copy()
        output_df_copy['geyezhangfu'] = output_df_copy['ts_code'].map(geyezhangfu)
        output_df_copy['geyezhanngfulv'] = (output_df_copy['geyezhangfu']-output_df_copy['close'])/output_df_copy['close']*100
        print(output_df_copy)
        time.sleep(0.1)
    output_dfs.append(output_df_copy)  # 将每个输出的DataFrame添加到列表中
    time.sleep(0.3)
# 输出所有保存的DataFrame
merged_df = pd.concat(output_dfs)
merged_df.to_excel(r'C:\Users\Administrator\Desktop\20cm_gailianng.xlsx', index=False)
print(merged_df)
