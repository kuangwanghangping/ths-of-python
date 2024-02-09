import time
from tqdm import tqdm

import pywencai
from crazy import *
import pandas as pd
from crazy import *
today = date.today()
today = today.strftime("%Y%m%d")#得到今天的日期

trade_date = get_transaction_date(20230101,20231218)
print(trade_date)
dataframe_completely_display()#dataframe完全展示
for i in trade_date:
    try:
        yes_stock = upstop_stock(i)['代码'].tolist()
        df = pywencai.get(query=f'{i}曾涨停,非st', loop=True)['xuangu_tableV1']  # 问财得到符合条件炸板的股票
        df['首次涨停时间'] = pd.to_datetime(df['首次涨停时间'])  # 将str格式转换为datetime格式
        # 筛选出首次涨停时间在09:30:00到09:31:30之间的行
        filtered_df = df[(df['首次涨停时间'] >= '09:30:00') & (df['首次涨停时间'] <= '09:31:30')]  # 过滤吊不符合条件的那几行
        # 打印筛选结果
        filtered_df = filtered_df[~filtered_df['code'].isin(upstop_stock(str(i))['代码'].tolist())]  # 过滤掉昨日涨停的
        filtered_df = filtered_df.loc[:, ['code', '股票代码']]
        print(i)
        print(filtered_df)
        time.sleep(5)
    except:
        pass
#











