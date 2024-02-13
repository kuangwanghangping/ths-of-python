from crazy import *
import tushare as ts
from tqdm import tqdm
dataframe_completely_display()
#获取2020年8月4日债券回购日行情
pro = ts.pro_api()
trade_list = get_transaction_date(20220811,20231231)
changes_dict = {}
#获取可转债行情
for i in tqdm(trade_list) :
    df = pro.cb_daily(trade_date=i)
    top_two_rows = df.nlargest(2, 'amount')['ts_code'].tolist()  # 得到成交量前二的股票
    daliy_premium = input_bond_list_date_out_premium(top_two_rows, i)
    changes_dict[i] = daliy_premium
print(changes_dict)


import pandas as pd
import matplotlib.pyplot as plt

# 初始值为100
value = 100

# 每日加减的数值字典，键为日期，值为加减的数值


# 将字典转换为DataFrame
changes_df = pd.DataFrame(list(changes_dict.items()), columns=['Date', 'Change'])
changes_df['Date'] = pd.to_datetime(changes_df['Date'])
changes_df = changes_df.sort_values('Date')

# 计算每日的累积值
cumulative_values = [value]
for _, row in changes_df.iterrows():
    value += row['Change']
    cumulative_values.append(value)

# 创建日期序列
dates = [pd.Timestamp('2024-01-01')] + list(changes_df['Date'])

# 创建折线图
plt.plot(dates, cumulative_values, marker='o')

# 添加标题和标签
plt.title('Daily Value Changes')
plt.xlabel('Date')
plt.ylabel('Value')

# 显示日期斜着显示
plt.xticks(rotation=45)

# 显示图表
plt.show()


