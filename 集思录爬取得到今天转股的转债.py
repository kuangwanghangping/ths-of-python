from tqdm import tqdm

import requests
import time
import threading
import tushare as ts
pro = ts.pro_api()
from crazy import *
dataframe_completely_display()
df = pro.cb_basic(fields="ts_code,bond_short_name,stk_code,stk_short_name,list_date,delist_date,remain_size")
all_bond_stock = dict(zip(df['ts_code'],df['bond_short_name']))
all_bond_stock = {bond.split('.')[0]: value for bond, value in all_bond_stock.items()}
print(all_bond_stock)
df = df[df['delist_date'].isna()]  # 前面两行是为了得到目前还在交易的转债，
bonds_list = df['ts_code'].tolist()
bonds_list = [bond.split('.')[0] for bond in bonds_list]
print(bonds_list)
all_scale_downing = {}
lock = threading.Lock()  # 创建锁对象，用于多线程对全局变量的访问
def get_scale_downing(bond):
    global all_scale_downing
    # 设置 GET 请求的参数
    url = f"https://www.jisilu.cn/data/cbnew/detail_hist/{bond}?___jsl=LST___t=1704707501648"  # 替换为您要请求的网址
    params = {"rp": 50, "page": 1}  # 替换为您的分页参数#这个是f12中载荷的表单数据字典格式填入
    # 发送 GET 请求并获取返回结果
    response = requests.post(url, params=params)
    # 打印返回的内容
    dict1 = response.json()['rows']
    list1 = []  # 用来保存前两天的数据
    for i in dict1:
        list1.append(i)
        # print(i)
    list1 = list1[:2]
    try:
        if list1[1]['cell']['curr_iss_amt'] != list1[0]['cell']['curr_iss_amt']:
            scale_downing = float(list1[1]['cell']['curr_iss_amt']) - float(list1[0]['cell']['curr_iss_amt'])
            with lock:  # 使用锁来保证对全局变量的安全访问
                all_scale_downing[bond] = scale_downing
    except:
        pass
start_time = time.time()
threads = []
for bond in tqdm(bonds_list):
    thread = threading.Thread(target=get_scale_downing, args=(bond,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
end_time = time.time()
print(all_scale_downing)
chinese_all_scale_downing = {}
for i ,ii  in all_scale_downing.items():
    if i in all_bond_stock.keys():
        chinese_all_scale_downing[all_bond_stock[i]] = ii
print(chinese_all_scale_downing)
print(end_time - start_time)
input("按下任意键退出")
