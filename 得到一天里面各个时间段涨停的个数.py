# import tushare as ts
# from crazy import *
# dataframe_completely_display()
# pro = ts.pro_api('522bd20d16a78ff247dd6c556103fa5cfdaf2076c918e08f99897374')
# trade_day = get_transaction_date(20230601,20240302)
# for i in trade_day:
#     df = pro.limit_list_d(trade_date=i, limit_type='U',
#                           fields='ts_code,trade_date,industry,name,close,pct_chg,first_time,up_stat,limit_times')
#     df['first_time'] = df['first_time'].astype(int)
#     # 根据条件分割 DataFrame
#     subset1 = df[(df['first_time'] > 93000) & (df['first_time'] < 100000)]
#     subset2 = df[(df['first_time'] > 100000) & (df['first_time'] < 103000)]
#     subset3 = df[(df['first_time'] > 103000) & (df['first_time'] < 110000)]
#     subset4 = df[(df['first_time'] > 110000) & (df['first_time'] < 113000)]
#     subset5 = df[(df['first_time'] > 130000) & (df['first_time'] < 133000)]
#     subset6 = df[(df['first_time'] > 133000) & (df['first_time'] < 140000)]
#     subset7 = df[(df['first_time'] > 140000) & (df['first_time'] < 143000)]
#     subset8 = df[(df['first_time'] > 143000) & (df['first_time'] < 150000)]
#

import pandas as pd
from crazy import *
import time
dataframe_completely_display()
# 初始化一个空的 DataFrame 用于存储所有数据
combined_df1 = pd.DataFrame()
combined_df2 = pd.DataFrame()
combined_df3 = pd.DataFrame()
combined_df4= pd.DataFrame()
combined_df5= pd.DataFrame()
combined_df6= pd.DataFrame()
combined_df7= pd.DataFrame()
combined_df8= pd.DataFrame()
combined_df9 = pd.DataFrame()
combined_df10 = pd.DataFrame()
combined_df11 = pd.DataFrame()
combined_df12= pd.DataFrame()
combined_df13= pd.DataFrame()
combined_df14= pd.DataFrame()
combined_df15= pd.DataFrame()
combined_df16= pd.DataFrame()
trade_day = get_transaction_date(20230325, 20240325)
print(trade_day)
subset1_list = []  # 用于存储每次循环得到的 subset1
subset2_list = []
subset3_list = []
subset4_list = []
subset5_list = []
subset6_list = []
subset7_list = []
subset8_list = []
subset9_list = []  # 用于存储每次循环得到的 subset1
subset10_list = []
subset11_list = []
subset12_list = []
subset13_list = []
subset14_list = []
subset15_list = []
subset16_list = []
for i in trade_day:
    df = pro.limit_list_d(trade_date=i, limit_type='U',
                          fields='ts_code,trade_date,industry,name,close,pct_chg,first_time,up_stat,limit_times')
    df['first_time'] = df['first_time'].astype(int)

    # 根据条件分割 DataFrame
    subset1 = df[(df['first_time'] > 93000) & (df['first_time'] < 94500)]
    subset1_list.append(subset1)  # 将 subset1 添加到列表中
    subset2 = df[(df['first_time'] > 94500) & (df['first_time'] < 100000)]
    subset2_list.append(subset2)
    subset3 = df[(df['first_time'] > 100000) & (df['first_time'] < 101500)]
    subset3_list.append(subset3)
    subset4 = df[(df['first_time'] > 101500) & (df['first_time'] < 103000)]
    subset4_list.append(subset4)
    subset5 = df[(df['first_time'] > 103000) & (df['first_time'] < 104500)]
    subset5_list.append(subset5)
    subset6 = df[(df['first_time'] > 104500) & (df['first_time'] < 110000)]
    subset6_list.append(subset6)
    subset7 = df[(df['first_time'] > 110000) & (df['first_time'] < 111500)]
    subset7_list.append(subset7)
    subset8 = df[(df['first_time'] > 111500) & (df['first_time'] < 113000)]
    subset8_list.append(subset8)
    subset9 = df[(df['first_time'] > 130000) & (df['first_time'] < 131500)]
    subset9_list.append(subset1)  # 将 subset1 添加到列表中
    subset10 = df[(df['first_time'] > 131500) & (df['first_time'] < 133000)]
    subset10_list.append(subset2)
    subset11 = df[(df['first_time'] > 133000) & (df['first_time'] < 134500)]
    subset11_list.append(subset3)
    subset12 = df[(df['first_time'] > 134500) & (df['first_time'] < 140000)]
    subset12_list.append(subset4)
    subset13 = df[(df['first_time'] > 140000) & (df['first_time'] < 141500)]
    subset13_list.append(subset5)
    subset14 = df[(df['first_time'] > 141500) & (df['first_time'] < 143000)]
    subset14_list.append(subset6)
    subset15 = df[(df['first_time'] > 143000) & (df['first_time'] < 144500)]
    subset15_list.append(subset7)
    subset16 = df[(df['first_time'] > 144500) & (df['first_time'] < 150000)]
    subset16_list.append(subset8)
    print(i)
    time.sleep(1)

# 将所有 subset1 合并成一个大的 DataFrame
combined_df1 = pd.concat(subset1_list)
combined_df2 = pd.concat(subset2_list)
combined_df3 = pd.concat(subset3_list)
combined_df4 = pd.concat(subset4_list)
combined_df5 = pd.concat(subset5_list)
combined_df6 = pd.concat(subset6_list)
combined_df7 = pd.concat(subset7_list)
combined_df8 = pd.concat(subset8_list)
combined_df9 = pd.concat(subset9_list)
combined_df10 = pd.concat(subset10_list)
combined_df11 = pd.concat(subset11_list)
combined_df12 = pd.concat(subset12_list)
combined_df13 = pd.concat(subset13_list)
combined_df14 = pd.concat(subset14_list)
combined_df15 = pd.concat(subset15_list)
combined_df16 = pd.concat(subset16_list)
# 打印合并后的 DataFrame

print(len(combined_df1['trade_date'].tolist()))
print(len(combined_df2['trade_date'].tolist()))
print(len(combined_df3['trade_date'].tolist()))
print(len(combined_df4['trade_date'].tolist()))
print(len(combined_df5['trade_date'].tolist()))
print(len(combined_df6['trade_date'].tolist()))
print(len(combined_df7['trade_date'].tolist()))
print(len(combined_df8['trade_date'].tolist()))
print(len(combined_df9['trade_date'].tolist()))
print(len(combined_df10['trade_date'].tolist()))
print(len(combined_df11['trade_date'].tolist()))
print(len(combined_df12['trade_date'].tolist()))
print(len(combined_df13['trade_date'].tolist()))
print(len(combined_df14['trade_date'].tolist()))
print(len(combined_df15['trade_date'].tolist()))
print(len(combined_df16['trade_date'].tolist()))
