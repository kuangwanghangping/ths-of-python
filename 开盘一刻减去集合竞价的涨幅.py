import time

from crazy import *
from tqdm import tqdm

df = pro.cb_basic(fields="ts_code,bond_short_name,stk_code,stk_short_name,list_date,delist_date,remain_size")
df = df[df['delist_date'].isna()]  # 前面两行是为了得到目前还在交易的转债，
df = df[df['remain_size'] != 0]
df = df[~df['list_date'].isna()]  # 删掉还没有可以上市交易的转债
stock_bond  = dict(zip(df['stk_code'], df['ts_code']))  # 这个是所有的可转债，历史上的也包括
list = []
for i in stock_bond:
    list.append(i)
list = list_strip_SZ_SH(list)
dataframe_completely_display()
import akshare as ak


for i in tqdm(list):
    stock_zh_a_hist_min_em_df = ak.stock_zh_a_hist_min_em(symbol=i, start_date="2024-03-29 09:30:00",
                                                          end_date="2024-03-29 15:00:00", period="1", adjust="")
    stock_zh_a_hist_min_em_df = stock_zh_a_hist_min_em_df.head(2)
    list = stock_zh_a_hist_min_em_df['开盘'].tolist()
    zhangfu = (list[-1] - list[0]) / list[0] * 100
    if zhangfu > 0.7:
        print(str(i) + " :"  + str(zhangfu))
    time.sleep(2)
