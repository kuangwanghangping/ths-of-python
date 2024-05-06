import json
import os
from crazy import *
# 指定要读取的文件路径
desktop_path = r'C:\Users\Administrator\Desktop'
file_path = os.path.join(desktop_path, "竞价成交额.json")
# 读取 JSON 文件并解析成字典格式
with open(file_path, "r") as file:
    data = json.load(file)#已经记录的信息
already_recorded_list = [i for i in data]
trade_list = get_transaction_date(20231101,20240505)#我想要记录的哪几天
unrecorded_list = list_diff (already_recorded_list,trade_list)
print(unrecorded_list)