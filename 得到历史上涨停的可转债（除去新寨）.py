import time
from tqdm import tqdm#进度条模块
from crazy import *
pro = ts.pro_api()
dataframe_completely_display()
#获取可转债行情
trade_date = get_transaction_date(20220618,20240213)#得到规定时间可以交易的日期
for i in tqdm(trade_date):
    df = pro.cb_daily(trade_date=i)#得到当日的可转债行情
    try:
        result = df[(df['pct_chg'] == 20) &(df['pre_close'] != 157.3)  & (df['pre_close'] != 188.76) ]#得到涨停的可转债
        if result.empty:
            pass
        else:
            print(result)
    except:
        pass
    time.sleep(0.1)

