import tushare as ts
pro = ts.pro_api()
from crazy import *
dataframe_completely_display ()
import pandas as pd
import time
import openpyxl
# from datetime import datetime
df = pro.ths_daily(ts_code='883910.TI', start_date='20231101', end_date='20231121', fields='ts_code,trade_date,open,close,high,low,pct_change')
# 将字符串日期转换为datetime对象
data_list  = df['trade_date'].tolist()      #获得这段时间可以交易的时间
print(data_list)
weidict = []
file_path = r'C:\Users\Administrator\Desktop\竞价程序\result.xlsx'
#不能直接写在桌面上因为，没有权限去直接修改里面的值，因为我想在一个xlsx里面一个sheet里面得到所有的值
workbook = openpyxl.Workbook()
worksheet = workbook.active
for date in range(len(data_list)):#这样我就能按照这个里面里面的顺序来得到里面的值，比如第一个，第二个
    if date == 0 or date == len(data_list) - 1:#我这样是为了删掉列表里面的第一行和最后一行
        #因为我最后合成的这个dataframe里面有用到前一天和后一天的内容
        continue
    try:
        qian_df = pro.cb_daily(trade_date=data_list[date - 1])
        jin_df = pro.cb_daily(trade_date=data_list[date])
        # hou_df = pro.cb_daily(trade_date=data_list[date + 1])
        merged_df = pd.merge(qian_df, jin_df, on='ts_code')
        #合成两个dataframe，按照里面的['ts_code']

        selected_cols = merged_df.loc[:, ['ts_code', 'trade_date_x', \
           'close_x', 'trade_date_y', 'open_y']]
        #这段是为了得到其他的脏数据#获得我自己想要的dataframe内容
        selected_cols['open_zhangfu'] = (selected_cols['open_y'] - selected_cols['close_x']) / selected_cols[
            'close_x'] * 100;
        top_two_rows = selected_cols.nlargest(2, 'open_zhangfu')
        #这段是得到我想要的按照open_zhangfu里面排行前二的两行
        # 写入Excel文件
        for index, row in top_two_rows.iterrows():
            worksheet.append(row.tolist())

        print(top_two_rows)
        time.sleep(3)
    except Exception as e:
        print("An error occurred:", str(e))
# 保存Excel文件
workbook.save(file_path)






