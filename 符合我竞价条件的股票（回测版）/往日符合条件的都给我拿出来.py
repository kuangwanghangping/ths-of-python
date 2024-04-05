import time

import tushare as ts
from crazy import *#from qmtpy import *
import datetime as dt
dataframe_completely_display()
import datetime
pro = ts.pro_api("522bd20d16a78ff247dd6c556103fa5cfdaf2076c918e08f99897374")
from crazy import *
jingjiazhangfu_data = read_jsonfile(r'C:\Users\Administrator\Desktop\jingjiazhangfu_data.json')
mount_data_data = read_jsonfile(r'C:\Users\Administrator\Desktop\mount_data.json')
def get_stock(date):
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    stock = []
    for i in data['ts_code'].tolist():
        if i.startswith('00') or i.startswith('60') or i.startswith('30'):
            stock.append(i)
    # 分割股票代码列表
    split_stock = [stock[i:i + 200] for i in range(0, len(stock), 200)]
    df_list = []
    for sublist in split_stock:
        sublist = ','.join(sublist)  # 将股票代码列表转换为逗号分隔的字符串
        df = pro.daily(ts_code=sublist, start_date=date,
                       end_date=date)
        df_list.append(df)
    result_df = pd.concat(df_list)
    result_df['increase_ratio'] = (result_df['high'] - result_df['close']) / result_df['pre_close']
    filtered_df = result_df[result_df['increase_ratio'] > 0.05]

    list = filtered_df['ts_code'].tolist()
    df = pro.limit_list_d(trade_date=date, limit_type='Z',
                          fields='ts_code,trade_date,industry,name,close,pct_chg,open_times,up_stat,limit_times')
    list1 = df['ts_code'].tolist()
    return list_union(list, list1)


data_list = get_transaction_date(20230220,20240330)
data_list = data_list[::-1]
print(data_list)
for date in range(len(data_list) - 1):
    satisfy_requiremment_stock_list = get_stock(data_list[date])
    for stock in satisfy_requiremment_stock_list:
        try:
            if 3< jingjiazhangfu_data[data_list[date + 1]][stock]<8 \
            and mount_data_data[data_list[date + 1]][stock] > 25000000:
                print(str(data_list[date + 1]) +"__"+  str(stock) +"++" +str(jingjiazhangfu_data[data_list[date + 1]][stock]))
        except:
            pass







