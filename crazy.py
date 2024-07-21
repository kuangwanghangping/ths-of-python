import re
import datetime
from datetime import date
import time
import json
import os
import requests
import akshare as ak
import json
from bs4 import BeautifulSoup
import tushare as  ts
pro = ts.pro_api("ad047441cc72120d3197505b58f84964148b449405d5e67b410a8bac")
import baostock as bs
import pandas as pd
import pywencai
from tqdm import tqdm
import threading
from threading import Lock
lg = bs.login()
def set_intersection (a,b):#两个set求交集
    set_result = a.intersection(b)
    return set_result
def set_union(a,b):
    union_set = a.union(b)
    return union_set
def set_diff (set_result,union_set):
    set_diff = set_result.symmetric_difference(union_set)
    return set_diff
def list_intersection (a,b):
    list_intersection = set(a) & set(b)
    list_result = list(list_intersection)
    return list_result
def list_union(a,b):
    list_result = list(set(a + b))
    return list_result
def list_diff (a,b):
    li_diff = [x for x in a if x not in b] + [x for x in b if x not in a]
    return li_diff
def filter_list(list1, list2):
    return [x for x in list1 if x not in list2]         #只要list2中有的，list1 就删除
def dict_intersection(dict1, dict2):
    intersection = {}
    for key in dict1.keys():
        if key in dict2 and dict1[key] == dict2[key]:
            intersection[key] = dict1[key]
    return intersection
def dict_union(dict1, dict2):
    dict_union = dict1.copy()
    dict_union.update(dict2)
    return dict_union

def dict_diff(dict1, dict2):
    dict_diff = {}
    for key in dict1.keys():
        if key not in dict2 or dict1[key] != dict2[key]:
            dict_diff[key] = dict1[key]
    for key in dict2.keys():
        if key not in dict1:
            dict_diff[key] = dict2[key]
    return dict_diff
def text_list (text):
    text1_list = set(text.split())
    text1_list = list(text1_list)
    return text1_list
def remove_dictionary_list_values(dictionary_list,list1):
    dictionary_list_value = {k: [value for value in v if value not in list1] for k, v in dictionary_list.items()}
    return dictionary_list_value
def text_append_sz_sh (text_stock):
    n_list = text_stock.strip().split('\n')
    for i in range(len(n_list)):
        if n_list[i].startswith('11') or n_list[i].startswith('60') or n_list[i].startswith('68'):
            n_list[i] += '.SH'
        if n_list[i].startswith('12') or n_list[i].startswith('30') or n_list[i].startswith('00'):
            n_list[i] += ".SZ"
    return n_list
def text_strip_sz_sh (text1_stock):
    n_list = text1_stock.strip().split('\n')
    for i in range(len(n_list)):
        n_list[i] = n_list[i][:-3]
    return n_list
def text_to_dict(text3):
    text_dict = {}
    lines = text3.split('\n')
    for line in lines:
        parts = line.split(' [')
        if len(parts) == 2:
            stock_name = parts[0].strip()
            concept_tags = parts[1].replace('[', '').replace(']', '').split(', ')
            concept_tags = [tag.strip("'") for tag in concept_tags]
            text_dict[stock_name] = concept_tags
    return text_dict
def dataframe_dict(dfname, dataframe_key, dataframe_value):
    result_dict1 = dfname[[dataframe_key, dataframe_value]].to_dict(orient='records')
    result4 = {item[dataframe_key]: item[dataframe_value] for item in result_dict1}
    return result4
#例如result = dataframe_dict(df,'股票代码','股票简称')
def list_strip_SZ_SH(list6):
    list7 = []
    for stk in list6 :
        list7.append(stk[:-3])
    return list7
def strip_list_element(list7, unwant_element):
    list8 = []
    for i in list7:
        if i != unwant_element:
            list8.append(i)
    return list8
def remove_source(text, text8):
    # 替换特殊字符为普通字符
    text8 = re.sub(r'([\[\](){}.+*?|^$\\])', r'\\\1', text8)
    # 替换数值部分为\\d+，匹配多个数字
    text8 = re.sub(r'\d+', r'\\d+', text8)
    # 替换空格为\\s+
    text8 = re.sub(r' ', r'\\s+', text8)
    # 替换冒号为:
    text8 = re.sub(r':', r':', text8)
    text99 = text8

    result = re.sub(text99, "", text)
    # 删除空白行
    result = re.sub(r'\n\s*\n', '\n', result)
    return result


def dictslist_list (dict29):
    ss = []
    for key, value in dict29.items():
        ss.append(value)
    new_list1 = []
    for sublist in ss:
        for item in sublist:
            new_list1.append(item)
    return new_list1
#{'节能国祯': ['国企改革', '地方国企改革', '节能环保', '新型城镇化', '央企国企改革'], '蓝天燃气': ['平安资管持股', '沪股通', '天然气管道', 'LNG加气站', '天然气']}
#['国企改革', '地方国企改革', '节能环保', '新型城镇化', '央企国企改革','平安资管持股', '沪股通', '天然气管道', 'LNG加气站', '天然气']
def reserve_dict_list_list (dict77,list20):
    result34 = {k: [v for v in dict77[k] if v in list20] for k in dict77}
    return result34
# dict77 = {'节能国祯': ['国企改革', '地方国企改革', '节能环保', '新型城镇化', '央企国企改革'], '蓝天燃气': ['平安资管持股', '沪股通', '天然气管道', 'LNG加气站', '天然气']}
# list20 = ['天然气', '平安资管持股']
#{'节能国祯': [], '蓝天燃气': ['平安资管持股', '天然气']}
def del_dict_list_list(dict27,list32):
    result43 = {k: [v for v in dict27[k] if v not in list32] for k in dict27}
    return result43
# dict77 = {'节能国祯': ['国企改革', '地方国企改革', '节能环保', '新型城镇化', '央企国企改革'], '蓝天燃气': ['平安资管持股', '沪股通', '天然气管道', 'LNG加气站', '天然气']}
# list20 = ['天然气', '平安资管持股']
#{'节能国祯': ['国企改革', '地方国企改革', '节能环保', '新型城镇化', '央企国企改革'], '蓝天燃气': ['沪股通', '天然气管道', 'LNG加气站']}


from collections import defaultdict

def calculate_avg_increase(concept_dict, increase_dict):
    concept_avg_price = defaultdict(list)
    for stock_code, concepts in concept_dict.items():
        if stock_code in increase_dict:
            stock_price = increase_dict[stock_code]
            for concept in concepts:
                concept_avg_price[concept].append(stock_price)
    for concept, prices in concept_avg_price.items():
        avg_price = sum(prices) / len(prices)
        concept_avg_price[concept] = avg_price
    return dict(concept_avg_price)
# concept_dict = {'000001.SZ': ['跨境支付（CIPS）', '标普道琼斯A股'], '000166.SZ': ['国企改革', '期货概念', '标普道琼斯A股']}
# price_dict = {'000001.SZ': 11.200000000000001, '000166.SZ': 4.33}
# avg_price_dict = calculate_avg_increase(concept_dict, price_dict)
# {'跨境支付（CIPS）': 11.200000000000001, '标普道琼斯A股': 7.765000000000001, '国企改革': 4.33, '期货概念': 4.33}




def calculate_price_increase(yest, today):
    price_increase = {}

    for stock_code, yest_price in yest.items():
        if stock_code in today:
            today_price = today[stock_code]
            increase = (today_price - yest_price) / yest_price
            price_increase[stock_code] = round(increase * 100, 2)

    return price_increase

# yest = {'000001.SZ': 11.200000000000001, '000166.SZ': 4.33}
# today = {'000001.SZ': 11.690000000000001, '000166.SZ': 4.29}
# price_increase_dict = calculate_price_increase(yest, today)
# print(price_increase_dict)
#{'000001.SZ': 4.38, '000166.SZ': -0.92}


def two_dict_trans_key2(stock_dict, industry_dict):
    result_dict = {}

    for stock_code, stock_name in stock_dict.items():
        if stock_name in industry_dict:
            result_dict[stock_code] = industry_dict[stock_name]

    return result_dict
#
# stock_dict = {'000001.SZ': '平安银行', '000166.SZ': '申万宏源'}
# industry_dict = {'平安银行': ['跨境支付（CIPS）', '标普道琼斯A股'], '申万宏源': ['国企改革', '期货概念', '标普道琼斯A股']}
# result = two_dict_trans_key(stock_dict, industry_dict)
# print(result)
#{'000001.SZ': ['跨境支付（CIPS）', '标普道琼斯A股'], '000166.SZ': ['国企改革', '期货概念', '标普道琼斯A股']}
def two_dict_trans_key1(stock_dict, industry_dict):
    result_dict = {}

    for stock_name, industry_list in industry_dict.items():
        if stock_name in stock_dict:
            stock_code = stock_dict[stock_name]
            result_dict[stock_code] = industry_list

    return result_dict
# n = {'平安银行': ['跨境支付（CIPS）', '标普道琼斯A股'], '申万宏源': ['国企改革', '期货概念', '标普道琼斯A股']}
# n1 = {'平安银行': '000001.SZ', '申万宏源': '000166.SZ','sss':shgu}
# result = two_dict_trans_key1(n1, n)
# print(result)
#{'000001.SZ': ['跨境支付（CIPS）', '标普道琼斯A股'], '000166.SZ': ['国企改革', '期货概念', '标普道琼斯A股']}
def dataframe_completely_display(display_columns=None, display_rows=None):
    import pandas as pd

    if display_columns is None:
        pd.set_option('display.max_columns', None)  # 显示所有列
    else:
        pd.set_option('display.max_columns', display_columns)

    if display_rows is None:
        pd.set_option('display.max_rows', None)  # 显示所有行
    else:
        pd.set_option('display.max_rows', display_rows)

    pd.set_option('display.width', None)  # 不限制显示宽度（自动换行）
def today_growth(yest_price, now_price):
    today_growth1 = {}
    for i, price in yest_price.items():
        growth = (now_price[i] - price) / price * 100
        today_growth1[i] = growth
    return today_growth1
#这个是算今天的涨幅的你需要输出两个字典一个是昨天的价格一个是今天的价格，就可以算出来了
def diff_dict_key(dict13,dict63):
    different_keys = set(dict13.keys()) ^ set(dict63.keys())
    return different_keys
#这个是两个字典找不同的键
# dict1 = {'ss': 23, 'sd': 37, 'dd': 72373}
# dict2 = {'ss': 25, 'dd': 839}
#
# different_keys = set(dict1.keys()) ^ set(dict2.keys())
# print(different_keys)
def aver_price(askPrice,askVol,bidPrice,bidVol):
    askresult = []
    bidresult = []
    for i in range(len(askPrice)):
        askresult.append(askPrice[i] * askVol[i])
    askresult = sum(askresult)
    for i in range(len(bidPrice)):
        bidresult.append(bidPrice[i] * bidVol[i])
    bidresult = sum(bidresult)
    all_m = bidresult + askresult
    all_vol = sum(askVol) + sum(bidVol)
    today_aver_price = all_m / all_vol
    return today_aver_price
def give_value_return_key(dict223,list3246):
    matching_keys = [key for key, value in dict223.items() if value in list3246]
    return matching_keys
def timestamp_to_Visual_time(timestamp):
    local_time = time.localtime(timestamp)

    # 格式化输出时间
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)

    return formatted_time

def get_transaction_date(start_date,end_date):
    import tushare as ts
    df456 = pro.ths_daily(ts_code='883910.TI', start_date=start_date, end_date=end_date, fields='ts_code,trade_date,open,close,high,low,pct_change')
# 将字符串日期转换为datetime对象
    data_list  = df456['trade_date'].tolist()      #获得这段时间可以交易的时间
    return data_list
def remove_the_inner_sublists_within_list(lists):
    result3456 = [item for sublist in lists for item in sublist]
    unique_list = list(set(result3456))
    return unique_list
    # 去除列表里面的小列表
def remove_list_duplicate_content(list387):
    unique_list = list(set(list387))
    return unique_list
def get_dict_key(my_dict,value_to_find):
    # 获取字典中所有键值对的元组列表
    items = my_dict.items()
    # 遍历元组列表，找到与给定值相等的值所对应的键
    for key, value in items:
        if value == value_to_find:
            return key
    #这个是输入一个字典和值，他会返回这个字典这个值对应的键

def judge_upstop_price(stock_name,stock_code,stock_yesterday_price):
    if stock_name.startswith(('st', '*st','ST', '*ST')) :
        # 这个是判断股票名字是否是st的，并且是不是主板的
        if stock_code.startswith(('00', '60')):
            upstop_price = round(stock_yesterday_price * 1.05,2)
        elif stock_code.startswith(('68', '30')):
            upstop_price = round(stock_yesterday_price * 1.2, 2)
        else:
            upstop_price = round(stock_yesterday_price * 1.3, 2)
    elif stock_name.startswith('N'):
        upstop_price = 100000#这个意思是无限大的意思
    elif stock_name.startswith('C'):
        upstop_price = 100000  # 这个意思是无限大的意思
    else:
        if stock_code.startswith(('00', '60')):
            upstop_price = round(stock_yesterday_price * 1.1,2)
        elif stock_code.startswith(('68', '30')):
            upstop_price = round(stock_yesterday_price * 1.2,2)
        else:
            upstop_price = round(stock_yesterday_price * 1.3,2)
    return upstop_price
#用来判断今日的涨停价格是多少
def judge_downstop_price(stock_name,stock_code,stock_yesterday_price):
    if stock_name.startswith(('st', '*st','ST', '*ST')) :
        # 这个是判断股票名字是否是st的，并且是不是主板的
        if stock_code.startswith(('00', '60')):
            downstop_price = round(stock_yesterday_price * 0.95,2)
        elif stock_code.startswith(('68', '30')):
            downstop_price = round(stock_yesterday_price * 0.8, 2)
        else:
            downstop_price = round(stock_yesterday_price * 0.7, 2)
    elif stock_name.startswith('N'):
        downstop_price = 1#这个意思是无限小的意思
    elif stock_name.startswith('C'):
        downstop_price = 1  # 这个意思是无限小的意思
    else:
        if stock_code.startswith(('00', '60')):
            downstop_price = round(stock_yesterday_price * 0.9,2)
        elif stock_code.startswith(('68', '30')):
            downstop_price = round(stock_yesterday_price * 0.8,2)
        else:
            downstop_price = round(stock_yesterday_price * 0.7,2)
    return downstop_price
#用来判断今日的跌停价格是多少
def get_month_range(year, month):
    start_date = datetime.date(year, month, 1)

    if month == 12:
        end_date = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
    else:
        end_date = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)

    return start_date.strftime("%Y%m%d"), end_date.strftime("%Y%m%d")
#我输入具体哪个月份，输出时间
#例如我输入(2023,12)，得到('20231201', '20231231')
def list_Element_Split(lsit):
    lsit1= []
    for item in lsit:
        lsit1.extend(item.split(';'))

    return lsit1
#['汽车电子;小鹏汽车概念;融资融券;专精特新;消费电子概念;PCB概念', '小额贷款;有色铝;一带一路;参股民营银行;光伏概念']
#['汽车电子','小鹏汽车概念','融资融券','专精特新','消费电子概念','PCB概念', '小额贷款','有色铝','一带一路','参股民营银行','光伏概念']
#print(input_stock_list_date_out_premium(['000001.SZ','600000.SH'], 20240207))
def input_stock_list_date_out_premium(list1, date):
    #输入股票代码和日期，算出隔夜的溢价。算法是隔夜价到第二天集合竞价的涨幅
    import datetime
    today = datetime.date.today()
    today_str = today.strftime("%Y%m%d")#获得今日日期
    tradeday_list = get_transaction_date(20000101, today_str)
    previous_date = None
    index = None
    date_str = str(date)
    if date_str in tradeday_list:
        index = tradeday_list.index(date_str)
        if index > 0:
            previous_date_str = tradeday_list[index - 1]
            previous_date = datetime.datetime.strptime(previous_date_str, "%Y%m%d").date()
    else:
        index = date_str
    ts_code_str = ','.join(list1)
    previous_date_str = previous_date.strftime("%Y%m%d") if previous_date else None
    df = pro.daily(ts_code=ts_code_str, start_date=previous_date_str, end_date=previous_date_str)
    df['geye_premium'] = (df['open']-df['pre_close'])/df['pre_close']*100
    a = sum(df['geye_premium'].tolist())/len(df['geye_premium'].tolist())
    return a

#print(input_stock_list_date_out_premium(['002783.SZ','603577.SH'],20231228))
#9.055098742005775

def input_stock_list_date_out_premium1(list1, date):#这个是输出字典版本的
    #输入股票代码和日期，算出隔夜的溢价。算法是隔夜价到第二天集合竞价的涨幅
    import datetime
    today = datetime.date.today()
    today_str = today.strftime("%Y%m%d")#获得今日日期
    tradeday_list = get_transaction_date(20000101, today_str)
    previous_date = None
    index = None
    date_str = str(date)
    if date_str in tradeday_list:
        index = tradeday_list.index(date_str)
        if index > 0:
            previous_date_str = tradeday_list[index - 1]
            previous_date = datetime.datetime.strptime(previous_date_str, "%Y%m%d").date()
    else:
        index = date_str
    ts_code_str = ','.join(list1)
    previous_date_str = previous_date.strftime("%Y%m%d") if previous_date else None
    df = pro.daily(ts_code=ts_code_str, start_date=previous_date_str, end_date=today_str)
    df['geye_premium'] = (df['open']-df['pre_close'])/df['pre_close']*100
    df = df.groupby('ts_code').tail(1)
    dict892347 = dict(zip(df['ts_code'],df['geye_premium']))
    return dict892347
#print(input_stock_list_date_out_premium1(['600491.SH','688599.SH'], 20231227))
#{'600491.SH': -0.4950495049505065, '688599.SH': -0.11485451761103038}
def dict_rank (dict7834):
# 按值对字典进行降序排序
    sorted_dict = sorted(dict7834.items(), key=lambda x: x[1], reverse=True)
# 创建包含所有键和排名的字典
    result_dict = {key: i + 1 for i, (key, _) in enumerate(sorted_dict)}
    return result_dict
#dict1 = {'hdjf': 123, 'gshjad': 2376, 'gydfjas': 2135, 'geyu': 6743}
#{'geyu': 1, 'gshjad': 2, 'gydfjas': 3, 'hdjf': 4}
def convert_to_yi(number):
    yi = number / 100000000
    return yi
#有时候一些数据很大，不直观，我有时候不知道是几个亿，
def last_trade_day():#这个是为了得到最近的交易日。这个是为了比如周日的时候得到的数据是星期五，
    today = datetime.date.today()
    today_str = today.strftime("%Y%m%d")#获得今日日期
    tradeday_list = get_transaction_date(20000101, today_str)
    return tradeday_list[0]
#print(last_trade_day())
#20240108
def last_trade_day_special(input_date):
    if type(input_date) == int:
        input_date = str(input_date)
    input_date = datetime.datetime.strptime(input_date, '%Y%m%d')
    today_str = input_date.strftime("%Y%m%d")#获得今日日期
    tradeday_list = get_transaction_date(20000101, today_str)
    return tradeday_list[1]
#date = last_trade_day_special('20240124')
#得到的是上一个交易日,如果你是星期六的话他给你的日期就是星期四的
def last_trade_day_special1(input_date):
    input_date1 = last_trade_day_special(input_date)
    from datetime import datetime
    current_date = datetime.now().strftime('%Y%m%d')
    input_date1 = datetime.strptime(input_date1, '%Y%m%d')
    today_str = input_date1.strftime("%Y%m%d")#获得今日日期
    tradeday_list = get_transaction_date(20000101, current_date)
    index = tradeday_list.index(today_str)
    previous_string = tradeday_list[index - 2]
    return previous_string
#print(last_trade_day_special1('20240201'))


def upstop_stock(date):#因为akshare2023年的涨停数据是丢失的，所以我用tushare更新了一下
    try:
        def add_suffix(code):
            if code.startswith('6'):
                return code + '.SH'
            elif code.startswith('0'):
                return code + '.SZ'
            else:
                return code + '.BJ'
        stock_zt_pool_previous_em_df = ak.stock_zt_pool_previous_em(date)
        stock_zt_pool_previous_em_df['代码'] = stock_zt_pool_previous_em_df['代码'].apply(add_suffix)
    except:
        stock_zt_pool_previous_em_df = pro.limit_list_d(trade_date=date, limit_type='U', fields='ts_code,trade_date,industry,name,close,pct_chg,open_times,up_stat,limit_times')
        stock_zt_pool_previous_em_df.rename(columns={'ts_code': '代码'}, inplace=True)

    return stock_zt_pool_previous_em_df

def crawler_inactivity_web(url):
    #url = "https://www.jisilu.cn/data/cbnew/detail_pic/?display=premium_rt&bond_id=123116"  # 替换为您要抓取的网页地址
    response = requests.get(url)

    # 使用 BeautifulSoup 解析网页内容
    soup = BeautifulSoup(response.text, "html.parser")
    dict_data = json.loads(str(soup))  # 这步是将soup格式转换为字典格式
    # 提取需要的数据
    # 这里假设您要抓取网页中的标题和正文内容
    return dict_data
#print(crawler_inactivity_web('https://www.jisilu.cn/data/cbnew/detail_pic/?display=premium_rt&bond_id=123116'))

def crawler_dynaics_web(url,params):
    #url = "https://www.jisilu.cn/data/cbnew/detail_hist/110083?___jsl=LST___t=1704707501648"  # 替换为您要请求的网址
    #params = {"rp": 50, "page": 1}  # 替换为您的分页参数#这个是f12中载荷的表单数据字典格式填入
    # 发送 GET 请求并获取返回结果
    response = requests.post(url, params=params)
    dict1 = response.json()
    return dict1
#print(crawler_dynaics_web("https://www.jisilu.cn/data/cbnew/detail_hist/110083?___jsl=LST___t=1704707501648",{"rp": 50, "page": 1}))



def name_suffix_transition(stock):#这个就是将有没有后缀的改变一下，有后缀的改成没有后缀的，没有后缀的改成有后缀的
    if (stock.startswith('00') or stock.startswith('30') or stock.startswith('12') and \
    stock.endswith('.SZ')) or (stock.startswith('60') or stock.startswith('68') or stock.startswith('11') and \
    stock.endswith('.SH')):
        stock = stock[:6]
    else:
        if stock.startswith('00') or stock.startswith('30') or stock.startswith('12') and \
            not stock.endswith('.SZ') :
            stock += '.SZ'
        elif stock.startswith('60') or stock.startswith('68') or stock.startswith('11') and \
            not stock.endswith('.SH'):
            stock += '.SH'
        else:
            stock += '.BJ'
    return stock
# print(name_suffix_transition('113920.SH'))
# print(name_suffix_transition('113920'))

def bond_redemp_to_stock_premium(bond):#可转债强行赎回的后，变成股票隔夜竞价就卖的溢价率
    data = crawler_inactivity_web(f'https://www.jisilu.cn/data/cbnew/detail_pic/?display=premium_rt&bond_id={bond}')
    that_day_premium = -data['picdata'][3][1]  # 那一天的利润可转债负溢价的利润
    that_day = data['picdata'][3][0]  # 2023-05-12
    new_date_str = that_day.replace("-", "")  # 那一天的日期20230512
    last_new_date = last_trade_day_special1(new_date_str)
    df = pro.cb_basic(fields="ts_code,bond_short_name,stk_code,stk_short_name,list_date,delist_date,remain_size")
    dict1 = dict(zip(df['ts_code'], df['stk_code']))  # 这个是所有的可转债，历史上的也包括
    bond_to_stock = name_suffix_transition(bond)
    df = pro.daily(ts_code=dict1[bond_to_stock], start_date=last_new_date, end_date=last_new_date)
    df['geye_premium'] = (df['open'] - df['pre_close']) / df['pre_close'] * 100
    stock_preium = df['geye_premium'].tolist()
    result = stock_preium[0] + that_day_premium
    return result
def input_bond_list_date_out_premium(list1, date):
    date1 = last_trade_day_special1(date)
    df = pro.cb_daily(trade_date=date1)
    df = df[df['ts_code'].isin(list1)]
    df['geye_premium'] = (df['open'] - df['pre_close']) / df['pre_close'] * 100
    try:
        df.loc[df['open'] == 0, 'geye_premium'] = bond_redemp_to_stock_premmium(
            (name_suffix_transition(','.join(df.loc[df['open'] == 0, 'ts_code'].astype(str)))))
    except:
        pass
    # 将'open'列的值为0对应的'geye_premium'列的值改为1

    result = sum(df['geye_premium'].tolist())/len(df['geye_premium'].tolist())
    return result
#print(input_bond_list_date_out_premium(['113595.SH','128143.SZ'],'20240207'))
def format_stock_code(code,output_type):
    if output_type == 'sz':
        if code.endswith('.SZ'):
            return 'sz' + code[:-3]
        else:
            return 'sh' + code[:-3]  # 这个为了akshare将123138.SZ变成sz123138
    elif output_type == "sz.":
        if code.endswith('.SZ'):
            return 'sz.' + code[:-3]
        else:
            return 'sh.' + code[:-3]  # 这个为了akshare将123138.SZ变成sz.123138


def input_bond_date_output_kill_in_end(stock,date):


    #这个函数是为了得到可转债的最后半小时是否出现了下杀的情况
    #但是不知道为啥，20231009之前的就无法访问
    import baostock as bs
    import pandas as pd
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
        result1 = 'yes'
    else:
        result1 = 'no'
    return result1
#print(input_bond_date_output_kill_in_end('128143.SZ','2024-02-07'))


#这两个用与两种时间之间的转换
def date_format_transform(date):
    # 检查输入日期的格式
    if '-' in date:  # 如果输入日期格式为 YYYY-MM-DD
        return date.replace('-', '')
    elif len(date) == 8:  # 如果输入日期格式为 YYYYMMDD
        return f"{date[:4]}-{date[4:6]}-{date[6:]}"
    else:
        return "Invalid date format"
# print(date_format_transform("20240207"))
# print(date_format_transform('2024-02-07'))
# 2024-02-07
# 20240207


def get_redeem_remain_days_equal_1():
    jsl_neirong = crawler_inactivity_web('https://www.jisilu.cn/webapi/cb/redeem/')['data']
    for i in jsl_neirong:
        if i['redeem_remain_days'] == 1:
            print(i)
        return i['bond_id']
    #print(get_redeem_remain_days_equal_1())这个是得到最后一天要宣布强赎与否的票，就是不隔夜
    #113063
def get_all_bonds(all):
    if all == 'historical' :
        df = pro.cb_basic(fields="ts_code,bond_short_name,stk_code,stk_short_name,list_date,delist_date,remain_size")
        dict1 = dict(zip(df['ts_code'], df['stk_code']))  # 这个是所有的可转债，历史上的也包括
    else:
        df = pro.cb_basic(fields="ts_code,bond_short_name,stk_code,stk_short_name,list_date,delist_date,remain_size")
        df = df[df['delist_date'].isna()]  # 前面两行是为了得到目前还在交易的转债，
        dict1 = dict(zip(df['ts_code'], df['stk_code']))
    return dict1
#你输入正股的形态，和日期就行了.就会得到对应的可转债
def base_on_pywc (query,date):
    get_all_bonds('historical')
    res = pywencai.get(query =f'{date}日{query}',loop=True)
    res = res['xuangu_tableV1']
    def add_suffix(code):
        if code.startswith('6'):
            return code + '.SH'
        elif code.startswith('0'):
            return code + '.SZ'
        else:
            return code + '.BJ'
    if res.empty:
        upstops_stock = ['000001.SZ']
    else:
        res['code'] = res['code'].apply(add_suffix)
        upstops_stock = res['code'].tolist()
    #print(upstops_stock)
    that_day_stock_upstops_bond = []
    for i,ii in get_all_bonds('historical').items():
        for n in upstops_stock:
            if ii == n :
                that_day_stock_upstops_bond.append(i)
    time.sleep(1)
    return that_day_stock_upstops_bond
# print(base_on_pywc('曾经涨停的股票','20240219'))
# ['113593.SH', '127099.SZ']
#如果你的字典是一个以日期为键的字典，该函数能得到字典里面键的下一天节约了重复爬取的时间
def get_dict_last_maxday(dict):
  from datetime import datetime, timedelta
  dict = {'20240220': 123, '20240221': 234, '20240222': 234, '20240229': 234}
  max_date = max(dict.keys())
  date_obj = datetime.strptime(max_date, '%Y%m%d')
  # 计算下一个日期
  next_date_obj = date_obj + timedelta(days=1)
  # 将下一个日期转换回字符串格式
  next_date = next_date_obj.strftime('%Y%m%d')
  return next_date
def dict_write_jsonfile(dictdata,path,name):
    file_path = os.path.join(path, f"{name}.json")
    with open(file_path, "w") as file:
        json.dump(dictdata, file)
    print(f"文件已经保存到{file_path}")
#（将什么字典数据，保存到哪，什么文件名字叫啥）

def read_jsonfile(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data
#输入地址的时候别让及r""例如r'C:\Users\Administrator\Desktop\jingjiazhangfu_data.json'





def dataframe_sort_by_column(df, sort_column_names, ascending=False):
    """
    根据指定列对DataFrame进行排序。

    Parameters:
    df (DataFrame): 输入的DataFrame。
    sort_column_names (str or list): 需要排序的列名，单个列名或列名的列表。
    ascending (bool, optional): 排序顺序，True表示升序，False表示降序。默认为True。

    Returns:
    DataFrame: 排序后的DataFrame。
    """
    df_sorted = df.sort_values(by=sort_column_names, ascending=ascending)
    return df_sorted
#dataframe删掉重复行
def dataframe_del_duplication_row(df, need_del_column_names):
    """
    删除DataFrame中重复的行。

    Parameters:
    df (DataFrame): 输入的DataFrame。
    need_del_column_names (list): 需要对标的列名，用于判断重复行。

    Returns:
    DataFrame: 删除重复行后的DataFrame。
    """
    return df.drop_duplicates(subset=need_del_column_names, keep='first', inplace=False)
def create_excel_from_list(type_output, data_list, output_path):
        # 列表生成excel的标签
    if type_output == "column":
       df = pd.DataFrame(data_list, columns=['Column1'])
    else:
        df = pd.DataFrame([data_list], columns=range(1, len(data_list) + 1))
    df.to_excel(output_path, index=False, header=False)
        # if __name__ == '__main__':
        #     output_file_path = r'C:\Users\Administrator\Desktop\output.xlsx'
        #     your_list = ['Apple', 'Orange', 'Banana', 'Grape', 'Pineapple']
        #     create_excel_from_list("column",your_list,output_file_path)
def is_within_time_range(date_int, start_date_str, end_date_str):
    # 用来判断一个时间是不是在另外两个时间之间
    # 主要用
    # 将日期字符串转换为日期时间对象
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    # 将整数日期转换为日期时间对象
    date = datetime.strptime(str(date_int), "%Y%m%d")

    # 检查给定日期是否在指定时间范围内
    if start_date <= date <= end_date:
        return True
    else:
        return False
# result = is_within_time_range(20030321, "2002-06-28", "2004-04-30")
# print(result)
def input_stock_list_date_out_premium_auction_to_auction (list1,date):
    import datetime
    today = datetime.date.today()
    today_str = today.strftime("%Y%m%d")#获得今日日期
    tradeday_list = get_transaction_date(20000101, today_str)
    previous_date = None
    index = None
    date_str = str(date)
    if date_str in tradeday_list:
        index = tradeday_list.index(date_str)
        if index > 0:
            previous_date_str = tradeday_list[index]
            last_date_str = tradeday_list[index - 1]
            previous_date = datetime.datetime.strptime(previous_date_str, "%Y%m%d").date()
            last_date = datetime.datetime.strptime(last_date_str, "%Y%m%d").date()
    else:
        index = date_str
    ts_code_str = ','.join(list1)
    last_date_str = previous_date.strftime("%Y%m%d") if previous_date else None
    previous_date_str= last_date.strftime("%Y%m%d") if last_date else None
    df = pro.daily(ts_code=ts_code_str, start_date=last_date_str, end_date=previous_date_str)
    return (df['open'].tolist()[0] - df['open'].tolist()[1])/df['open'].tolist()[1] * 100


def parse_data_to_dict(data: str) -> dict:
    # 创建一个空字典来存储解析后的数据
    parsed_dict = {}
#这个多用在开盘啦里面body
    # 按照每行进行拆分
    lines = data.split("\n")
    # 对每一行进行处理
    for line in lines:
        # 去除首尾空白
        line = line.strip()
        # 跳过空行
        if not line:
            continue

        # 将行分割为键和值
        key, value = line.split("\t")

        # 将键和值存储在字典中
        parsed_dict[key] = value

    return parsed_dict


def sort_list2_by_list1_order(list1, list2):
    """
    根据list1中元素的顺序对list2进行排序

    参数:
    list1 (list): 要用于排序的参考列表
    list2 (list): 要排序的列表

    返回:
    list: 排序后的list2，其中元素按照在list1中首次出现的顺序排列
    """
    # 创建一个字典来存储list1中元素的索引
    index_dict = {element: idx for idx, element in enumerate(list1)}

    # 创建一个列表来存储排序后的元素
    sorted_list2 = []

    # 遍历list2，根据在list1中的索引进行排序
    for element in list2:
        # 如果元素在index_dict中，则添加到sorted_list2中
        if element in index_dict:
            sorted_list2.append((index_dict[element], element))
            # 如果元素不在list1中，则将其索引设为无穷大（或其他大于list1长度的数）
        else:
            sorted_list2.append((float('inf'), element))

            # 根据索引进行排序，然后仅返回元素部分
    return [elem for _, elem in sorted(sorted_list2)]
def get_before_day(input_date):
    index = date_list.index(input_date)#date_list = get_transaction_date(20240302, 20240325)我这里面是全局变量
    return date_list[index+1]

def get_today_price_minus_yes_price(stockID,date):
    yes_date = get_before_day(date)
    url = 'https://apphis.longhuvip.com/w1/api/index.php'
    headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N976N Build/QP1A.190711.020)'}
    yes_data = f"""a	GetStockTrend
               apiv	w36
               c	StockL2History
               StockID	{stockID}
               PhoneOSNew	1
               UserID	0
               DeviceID	ffffffff-d151-c2cd-0000-00002cd5753b
               VerSion	5.14.0.0
               Token	0
               Day	{yes_date}"""
    yes_datas = parse_data_to_dict(yes_data)
    response = requests.post(url, data=yes_datas, headers=headers)
    response.encoding = response.apparent_encoding
    yes_data = json.loads(response.text)
    yes_data = yes_data['begin_px']
    data = f"""a	GetStockTrend
               apiv	w36
               c	StockL2History
               StockID	{stockID}
               PhoneOSNew	1
               UserID	0
               DeviceID	ffffffff-d151-c2cd-0000-00002cd5753b
               VerSion	5.14.0.0
               Token	0
               Day	{date}"""
    datas = parse_data_to_dict(data)
    response = requests.post(url, data=datas, headers=headers)
    response.encoding = response.apparent_encoding
    data = json.loads(response.text)
    data = data['begin_px']
    return ((data-yes_data)/yes_data)*100
def get_all_bankua():
    url = 'https://apphwhq.longhuvip.com/w1/api/index.php'
    headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N976N Build/QP1A.190711.020)'}
    bankua_list = []
    lock = Lock()  # 创建一个锁来确保线程安全
    threads = []
    # 定义fetch_bankua函数，但这次是在get_all_bankua内部
    def fetch_bankua(i, bankua_list, lock):
        data = f"""  
        Order	1  
        a	RealRankingInfo  
        st	30  
        c	ZhiShuRanking  
        PhoneOSNew	1  
        RStart	0925  
        DeviceID	ffffffff-d151-c2cd-0000-00002cd5753b  
        VerSion	5.14.0.4  
        Index	{i * 30}  
        REnd	1500  
        apiv	w36  
        Type	5  
        ZSType	5  
        """
        datas = parse_data_to_dict(data)  # 确保这个函数能正确解析数据
        response = requests.post(url, data=datas, headers=headers)
        response.encoding = response.apparent_encoding
        if response.status_code == 200:
            data_list = json.loads(response.text)['list']
            with lock:
                for item in data_list:
                    bankua_list.append(item[0])
                    # 创建并启动线程
    for i in range(14):
        t = threading.Thread(target=fetch_bankua, args=(i, bankua_list, lock))
        t.start()
        threads.append(t)
        # 等待所有线程完成
    for t in threads:
        t.join()
        # 打印并返回结果
    return bankua_list




if __name__ == '__main__':
   print(upstop_stock(20230206))
   # print(upstop_stock(20240205))
   #  dataframe_completely_display()
   #  input_stock_list_date_out_premium1(['002261.SZ'], 20230224)









