import time

import tushare as ts
pro = ts.pro_api()
from crazy import *
dataframe_completely_display()
df = pro.cb_basic(fields="ts_code,bond_short_name,stk_code,stk_short_name,list_date,delist_date,remain_size")
df = df[df['delist_date'].isna()]#前面两行是为了得到目前还在交易的转债，
remain_size_dict  = dict(zip(df['ts_code'],df['remain_size']))#将还在交易的转债做成字典键是转债代码，值是剩余规模
bonds_name = dict(zip(df['ts_code'],df['bond_short_name']))#得到转债的中文名，后面他没有只能自己加上去
df1 = pro.cb_daily(trade_date=last_trade_day())
df1['remain_size'] = df1['ts_code'].map(remain_size_dict)
df1['bonds_name'] = df1['ts_code'].map(bonds_name)
df1['转债市值'] = df1['remain_size'] * df1['close']/100
df1 = df1[~(df1['vol'] == 0)]#得到['vol']不等于0的，因为有些转债还在但是以后都不会交易了
df1 = df1.sort_values('转债市值', ascending=True)#顺序排列
top_10 = df1.head(10)#得到前十名]
stock_dict = dict(zip(top_10['bonds_name'],top_10['转债市值']))
time.sleep(10)
for i ,ii  in stock_dict.items():
    stock_dict[i] = convert_to_yi(ii)
print(stock_dict)
