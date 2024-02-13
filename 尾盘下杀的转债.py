from crazy import *
import tushare as ts
from tqdm import tqdm
import akshare as ak
import time
dataframe_completely_display()



#### 登陆系统 ####
#2023-10-09
def input_bond_date_output_kill_in_end(stock,date):
    #这个函数是为了得到可转债的最后半小时是否出现了下杀的情况
    #但是不知道为啥，20231009之前的就无法访问

    stock = format_stock_code(stock, 'sz.')
    rs = bs.query_history_k_data_plus(stock,
                                      "date,time,code,high,low,open,close,volume,amount,adjustflag",
                                      start_date=date, end_date=date,
                                      frequency="30", adjustflag="3")
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    if -(float(result['close'].tolist()[-1]) - float(result['close'].tolist()[-2])) / float(
            result['close'].tolist()[-2]) * 100 > 3.8:
        result = 'yes'
    else:
        result = 'no'
    return result
#print(input_bond_date_output_kill_in_end('128143.SZ','2024-02-07'))


pro = ts.pro_api()
trade_list = get_transaction_date(20231010,20240213)
print(trade_list)
#得到转债尾盘下杀的转债
for i in trade_list :
    df = pro.cb_daily(trade_date=i)
    top_ten_rows = df.nlargest(3, 'amount')['ts_code'].tolist()  # 得到成交量前十的股票
    for bond in top_ten_rows:
        time.sleep(0.2)

        if input_bond_date_output_kill_in_end(bond, date_format_transform(i)) == 'yes':
            print(i + '   ' + bond)
        else:
            pass



