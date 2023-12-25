import time

import tushare as ts
from crazy import *
import pandas as pd
dataframe_completely_display ()
pro = ts.pro_api()
from datetime import datetime

for i in range(1, 13):
    success = False
    while not success:
        try:
            date1, date2 = get_month_range(2022, i)
            date = get_transaction_date(date1, date2)
            upstop_count = []
            trade_days = 0
            for d in date:
                df = pro.limit_list_d(trade_date=d, limit_type='U',
                                      fields='ts_code,trade_date,industry,name,close,pct_chg,open_times,up_stat,limit_times')
                date_count = len(df['ts_code'].tolist())
                date_count = float(date_count)
                upstop_count.append(date_count)
                trade_days = trade_days + 1
                time.sleep(1)
            print(f'{i}月涨停的列表：{upstop_count}')
            print(f'{i}月涨停的总个数：{sum(upstop_count)}')
            print(f'{i}月交易的天数：{trade_days}')
            print(f'{i}月交易的平均涨停数目：{sum(upstop_count) / trade_days}')
            success = True  # 成功执行后将 success 设为 True
        except Exception as e:
            print(f"发生异常：{e}，正在重试...")
            time.sleep(1)  # 等待1秒



