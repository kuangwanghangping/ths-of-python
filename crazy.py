import re
def set_intersection (a,b):#两个set求交集
    set_result = a.intersection(b)
    return set_result
def set_union(a,b):
    union_set = a.union(b)
    return union_set
def set_diff (set_result,union_set):
    set_diff = set_result.symmetric_difference(union_set)
    return list(set_diff)
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
# n1 = {'平安银行': '000001.SZ', '申万宏源': '000166.SZ'}
# result = two_dict_trans_key1(n1, n)
# print(result)
#{'000001.SZ': ['跨境支付（CIPS）', '标普道琼斯A股'], '000166.SZ': ['国企改革', '期货概念', '标普道琼斯A股']}
def dataframe_completely_display ():
    import pandas as pd
    pd.set_option('display.max_columns', None)  # 显示所有列
    pd.set_option('display.max_rows', None)  # 显示所有行
    pd.set_option('display.width', None)  # 不限制显示宽度（自动换行）

def give_value_return_key(dict223,list3246):
    matching_keys = [key for key, value in dict223.items() if value in list3246]
    return matching_keys