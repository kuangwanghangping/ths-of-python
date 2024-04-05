import time
import os
import json
import pywencai
from crazy import *
dataframe_completely_display()
import pandas as pd
def get_word_result(word='今日创业板的竞价成交额'):
    df=pywencai.get(question=word,loop=True)
    return df
want_get_data = get_transaction_date(20230220,20240330)
dict_mount = {}
dict_jingjiazhangfu = {}
for i in tqdm(want_get_data):
    df = get_word_result(str(i) + "日股票的竞价成交额")
    try:
        dict22 = dict(zip(df['股票代码'], df[f'竞价金额[{i}]']))
        dict11 = dict(zip(df['股票代码'], df[f'竞价涨幅[{i}]']))
        dict_mount[i] = dict22
        dict_jingjiazhangfu[i] = dict11
    except:
        pass

    time.sleep(30)

desktop_path = r'C:\Users\Administrator\Desktop'
mount_file_path = os.path.join(desktop_path, "mount_data.json")
jingjiazhangfu_file_path = os.path.join(desktop_path, "jingjiazhangfu_data.json")
# 将字典保存为 JSON 文件
with open(mount_file_path, "w") as file:
    json.dump(dict_mount, file)
with open(jingjiazhangfu_file_path, "w") as file:
    json.dump(dict_jingjiazhangfu, file)
print(dict_mount)
print(dict_jingjiazhangfu)
