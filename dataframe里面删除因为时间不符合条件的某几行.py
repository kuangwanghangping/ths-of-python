import pywencai
from crazy import *
import pandas as pd
from crazy import *
dataframe_completely_display()
df = pywencai.get(query = '今日曾涨停',loop=True)['xuangu_tableV1']
df['首次涨停时间'] = pd.to_datetime(df['首次涨停时间'])
# 筛选出首次涨停时间在09:30:00到09:31:30之间的行
filtered_df = df[(df['首次涨停时间'] >= '09:30:00') & (df['首次涨停时间'] <= '09:31:30')]
# 打印筛选结果
print(filtered_df)