from crazy import *
dataframe_completely_display()
date_list = get_transaction_date(20240302, 20240325)
###############################################################################
def get_yesterday_bankua(input_date):  # 这个函数是我输入今天的日期，得到今天不能交易的股票
    datas = {'Order': '1', 'a': 'RealRankingInfo', 'st': '71', 'c': 'ZhiShuRanking', 'PhoneOSNew': '1',
             'DeviceID': 'ffffffff-d151-c2cd-0000-00002cd5753b', 'VerSion': '5.14.0.0', 'Index': '0',
             'Date': last_trade_day_special(input_date), 'apiv': 'w36', 'Type': '10', 'ZSType': '5'}
    headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N976N Build/QP1A.190711.020)'}
    url = 'https://apphis.longhuvip.com/w1/api/index.php'
    response = requests.post(url, data=datas, headers=headers)
    response.encoding = response.apparent_encoding
    data = json.loads(response.text)
    cannot_trade_stock_list = []
    can_trade_stock_list = []
    for i in data['list']:
        if i[3] > 2.5:
            cannot_trade_stock_list.append(i[1])
        else:
            can_trade_stock_list.append(i[1])
    return cannot_trade_stock_list


def get_bankua(input_date):  # 这个是输入指定日期，输出该日子的竞价按照板块成交额排序的的板块
    url = 'https://apphis.longhuvip.com/w1/api/index.php'
    headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N976N Build/QP1A.190711.020)'}
    datas = parse_data_to_dict(f"""Order	1
st	60
a	RealRankingInfo
c	ZhiShuRanking
PhoneOSNew	1
RStart	0925
DeviceID	ffffffff-d151-c2cd-0000-00002cd5753b
VerSion	5.14.0.0
Index	0
Date	{date_format_transform(input_date)}
REnd	0930
apiv	w36
Type	4
ZSType	5

	""")
    response = requests.post(url, data=datas, headers=headers)
    response.encoding = response.apparent_encoding
    data = json.loads(response.text)
    list2 = data['list']

    return list2  # [i[0] for i in list2],[i[3] for i in list2]
def get_stock(PlateID, input_date):  # 输入板块的id和日期得到当日的板块因为我是竞价买票，
    # 所以需要考虑的是竞价的时候这个板块有没有这个股票
    url = 'https://apphis.longhuvip.com/w1/api/index.php'
    headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N976N Build/QP1A.190711.020)'}
    data = f"""	
a	ZhiShuStockList_W8
apiv	w36
c	ZhiShuRanking
Date	{date_format_transform(input_date)}
DeviceID	ffffffff-d151-c2cd-0000-00002cd5753b
Index	0
IsKZZType	0
IsZZ	0
old	1
Order	1
PhoneOSNew	1
PlateID	{PlateID}
REnd	0930
RStart	0925
st	30
Token	0
Type	1
UserID	0
VerSion	5.14.0.0"""
    datas = parse_data_to_dict(data)
    response = requests.post(url, data=datas, headers=headers)
    response.encoding = response.apparent_encoding
    data = json.loads(response.text)
    return data
def input_plateid_data_getstock(input_date):
    can_not_trade_list = get_yesterday_bankua(input_date)
    excluded_strings = ['融资融券', '参股银行', '标普道琼斯A股', '富时罗素概念股', 'MSCI概念', '沪股通', '黄金概念',
                        '深股通', '证金持股', '同花顺漂亮100', '高送转预期', '人民币贬值受益', '专精特新']
    get_bank_stock = []
    print('得到今天竞价成交额板块的排序'+str([i[1] for i in get_bankua(input_date)]))
    for i in get_bankua(input_date):
        if i[3] > 0 and i[9] > 3 and i[1] not in excluded_strings and i[1] not in can_not_trade_list:
            stock_data = get_stock(i[0], input_date)
            stock_data = stock_data['list']
            stock_list = [i[0] for i in stock_data]
            get_bank_stock += stock_list
    return get_bank_stock
def get_word_result(word='今日创业板的竞价成交额'):
    df = pywencai.get(question=word, loop=True)
    return df
def get_ths_stock(input_date):
    yesterday = last_trade_day_special(input_date)
    try:
        list4 = get_word_result(f'{input_date}竞价成交额大于{yesterday}竞价成交额的两倍，{input_date}竞价成交额大于1000万，市值小于300亿，{input_date}竞价涨停的除外，{input_date}竞价跌停的也不要，非st，{yesterday}未涨停也未曾涨停,{input_date}竞价大幅高开')['股票代码'].tolist()
        print(list4)
    except:
        list4 = []
    time.sleep(10)
    try:
        list1 = get_word_result(f'{input_date}竞价成交额大于{yesterday}竞价成交额的两倍，{input_date}竞价成交额大于1000万，市值小于300亿，{input_date}竞价涨停的除外，{input_date}竞价跌停的也不要，非st，{yesterday}未涨停也未曾涨停,{input_date}竞价抢筹')['股票代码'].tolist()
        print(list1)
    except:
        list1 = []
    time.sleep(10)
    try:
        list3 = get_word_result(f'{input_date}竞价成交额大于{yesterday}竞价成交额的两倍，{input_date}竞价成交额大于3000万，市值小于300亿，{input_date}竞价涨停的除外，{input_date}竞价跌停的也不要，非st，{yesterday}未涨停也未曾涨停')['股票代码'].tolist()
        print(list3)
    except:
        list3 = []
    list1 = list3 + list1 + list4
    list2 = [name_suffix_transition(i) for i in list1]
    return list2
def get_intersection(input_date):
    get_bank_stock=input_plateid_data_getstock(input_date)
    print('这个是开盘啦选出的'+str(get_bank_stock))
    list2 = get_ths_stock(input_date)
    list2 = list_intersection(get_bank_stock, list2)
    return list2
print(get_intersection('20240506'))
