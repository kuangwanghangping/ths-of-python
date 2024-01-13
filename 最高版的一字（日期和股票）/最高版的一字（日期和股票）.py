import tushare as ts
pro = ts.pro_api()
import pandas as pd
from crazy import *
dataframe_completely_display()
trade_day = get_transaction_date(20230101,20240111)
trade_day = trade_day[::-1]
result_list = []
for i in range(len(trade_day)-1):
    if i != 0 or i != len(trade_day) - 2 or i != len(trade_day) - 1:
        # 得到最高版的股票和几板
        df = pro.limit_list_d(trade_date=trade_day[i], limit_type='U', fields='ts_code,trade_date,name,limit_times')
        df = df.sort_values('limit_times', ascending=True)
        max_limit_times = df['limit_times'].max()
        max_rows = df[df['limit_times'] == max_limit_times]
        # 输出最后一行或所有等于最大值的行
        if len(max_rows) == 1:
            output = pd.DataFrame(max_rows.iloc[-1]).T
        else:
            output = max_rows
        the_highest = dict(zip(output['ts_code'], output['limit_times']))
        # 得到最高版的股票和几板
        df = pro.limit_list_d(trade_date=trade_day[i+1], limit_type='U', fields='ts_code,first_time')
        df['first_time'] = pd.to_numeric(df['first_time'], errors='coerce')  # 这个是为了将first_time变成可以计算的int
        df = df[df['first_time'] <= 93000]
        geyeupstop_list = df['ts_code'].tolist()
        for it, ii in the_highest.items():
            if it in geyeupstop_list:
                result_list.append(str(trade_day[i] + ' : ' +  it))
                print(trade_day[i])
    time.sleep(1.5)
print(result_list)


