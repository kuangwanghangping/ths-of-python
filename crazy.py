import re
import datetime
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
def dataframe_completely_display ():
    import pandas as pd
    pd.set_option('display.max_columns', None)  # 显示所有列
    pd.set_option('display.max_rows', None)  # 显示所有行
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


    timestamp1 = timestamp / 1000

    # 将秒级别时间戳转换为日期时间对象
    dt_object = datetime.datetime.fromtimestamp(timestamp1)
    return dt_object

def get_transaction_date(start_date,end_date):
    import tushare as ts
    pro = ts.pro_api('e3157f092f921a4b8ff61524559de8681fb81a56e65f14297e47824e')
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
def get_month_range(year, month):
    start_date = datetime.date(year, month, 1)

    if month == 12:
        end_date = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
    else:
        end_date = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)

    return start_date.strftime("%Y%m%d"), end_date.strftime("%Y%m%d")
#我输入具体哪个月份，输出时间
#例如我输入(2023,12)，得到('20231201', '20231231')