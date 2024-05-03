import time
import os
import json
import pywencai
from crazy import *
import matplotlib.pyplot as plt
dataframe_completely_display()
import pandas as pd
def get_word_result(word='今日创业板的竞价成交额'):
    df=pywencai.get(question=word,loop=True)
    return df
start_date = '20240420'
end_date = '20240424'
date_dict = {}
date = get_transaction_date(int(start_date),int(end_date))
for i in date:
    print(i)
    everyday_amount = {}
    everyday_amount = dict(zip(get_word_result(f'{i}股票的竞价成交额')['股票代码'], get_word_result(f'{i}股票的竞价成交额')[f'竞价金额[{i}]']))
    date_dict[i] = everyday_amount
    time.sleep(10)
desktop_path = r'C:\Users\Administrator\Desktop'
file_path = os.path.join(desktop_path, "竞价成交额.json")
# 将字典保存为 JSON 文件
with open(file_path, "w") as file:
    json.dump(date_dict, file)
print("文件已保存到桌面:", file_path)
