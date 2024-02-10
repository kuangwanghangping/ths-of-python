import time
from tqdm import tqdm

import pywencai
from crazy import *
import pandas as pd
from crazy import *
today = date.today()
today = today.strftime("%Y%m%d")#得到今天的日期


trade_date = get_transaction_date(20230110,20231218)
print(trade_date)
dataframe_completely_display()#dataframe完全展示
for i in range(1, len(trade_date)-1):
    try:
        yes_stock = upstop_stock(trade_date[i+1])['代码'].tolist()
        yes_stock = [x[:-3] for x in yes_stock]
        df = pywencai.get(query=f'{trade_date[i]}曾涨停,非st', loop=True)['xuangu_tableV1']  # 问财得到符合条件炸板的股票
        df['首次涨停时间'] = pd.to_datetime(df['首次涨停时间'])  # 将str格式转换为datetime格式
        # 筛选出首次涨停时间在09:30:00到09:31:30之间的行
        filtered_df = df[(df['首次涨停时间'] >= '09:30:00') & (df['首次涨停时间'] <= '09:31:30')]  # 过滤不符合条件的行
        filtered_df.reset_index(drop=True, inplace=True)  # 重置索引
        # 过滤掉昨日涨停股票
        filtered_df = filtered_df[~filtered_df['code'].isin(yes_stock)]
        filtered_df = filtered_df.loc[:, ['code', '股票代码']]
        if filtered_df.empty:
            pass
        else:
            print(trade_date[i])
            print(filtered_df)
        time.sleep(5)

    except:
        pass

