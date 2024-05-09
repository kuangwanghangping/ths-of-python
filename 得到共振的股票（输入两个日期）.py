from crazy import *
dataframe_completely_display()
from crazy import *
date_list = get_transaction_date(20240302, 20240325)
kpl_date_list = [i[:4] + '-' + i[4:6] + '-' + i[6:] for i in date_list]
def ths_kpl(excoordinates_date, coordinates_date):
    def get_coordinates_date_stock(excoordinates_date, coordinates_date):
        def get_yesterday_bankua(excoordinates_date):
            datas = {'Order': '1', 'a': 'RealRankingInfo', 'st': '71', 'c': 'ZhiShuRanking', 'PhoneOSNew': '1',
                     'DeviceID': 'ffffffff-d151-c2cd-0000-00002cd5753b', 'VerSion': '5.14.0.0', 'Index': '0',
                     'Date': excoordinates_date, 'apiv': 'w36', 'Type': '10', 'ZSType': '5'}
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
        def get_bankua(coordinates_date):
            url = 'https://apphis.longhuvip.com/w1/api/index.php'
            headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N976N Build/QP1A.190711.020)'}
            datas = {'Order': '1', 'st': '30', 'a': 'RealRankingInfo', 'c': 'ZhiShuRanking', 'PhoneOSNew': '1',
                     'RStart': '0925', 'DeviceID': 'ffffffff-d151-c2cd-0000-00002cd5753b', 'VerSion': '5.14.0.0',
                     'Index': '0', 'Date': coordinates_date, 'REnd': '0930', 'apiv': 'w36', 'Type': '-4', 'ZSType': '5'}
            response = requests.post(url, data=datas, headers=headers)
            response.encoding = response.apparent_encoding
            data = json.loads(response.text)
            return data['list']
        def get_stock(PlateID):
            url = 'https://apphq.longhuvip.com/w1/api/index.php'
            headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N976N Build/QP1A.190711.020)'}
            datas = {'VerSion': '5.14.0.0', 'UserID': '0', 'Type': '8', 'Token': '0', 'st': '30', 'RStart': '0925', 'REnd': '0930', 'PlateID': {PlateID}, 'PhoneOSNew': '1', 'Order': '1', 'old': '1', 'IsZZ': '0', 'IsKZZType': '0', 'Index': '0', 'DeviceID': 'ffffffff-d151-c2cd-0000-00002cd5753b', 'c': 'ZhiShuRanking', 'apiv': 'w36', 'a': 'ZhiShuStockList_W8'}

            response = requests.post(url, data=datas, headers=headers)
            response.encoding = response.apparent_encoding
            data = json.loads(response.text)
            return data
        can_not_trade_list = get_yesterday_bankua(excoordinates_date)
        excluded_strings = ['融资融券', '参股银行', '标普道琼斯A股', '富时罗素概念股', 'MSCI概念', '沪股通', '深股通',
                            '证金持股', '同花顺漂亮100', '高送转预期', '人民币贬值受益', '专精特新']
        get_bank_stock = []
        for i in get_bankua(coordinates_date):
            if i[3] > 0 and i[9] > 3 and i[1] not in excluded_strings and i[1] not in can_not_trade_list:
                # print(str(i[0]) + str(i[1]))
                # print(get_stock(i[0])['list'])
                list_length = len(get_stock(i[0])['list'])
                for ii in range(list_length):
                    get_bank_stock.append(get_stock(i[0])['list'][ii][0])
        print(get_bank_stock)
        return get_bank_stock
    list1 = get_coordinates_date_stock(excoordinates_date, coordinates_date)
    list1 = [name_suffix_transition(i) for i in list1]
    def get_word_result(word='今日创业板的竞价成交额'):
        df = pywencai.get(question=word, loop=True)
        return df
    def get_ths_stock(excoordinates_date, coordinates_date):
        stock_list = get_word_result(
            f'{coordinates_date}日竞价成交额大于{excoordinates_date}日竞价成交额的两倍，{coordinates_date}日竞价成交额大于1000万，市值小于300亿，{coordinates_date}日竞价涨停的除外，{coordinates_date}日竞价跌停的也不要，非st，{excoordinates_date}日未涨停也未曾涨停,{coordinates_date}日竞价抢筹')['股票代码'].tolist()
        time.sleep(10)
        stock_list1 = get_word_result(
            f'{coordinates_date}日竞价成交额大于{excoordinates_date}日竞价成交额的两倍，{coordinates_date}日竞价成交额大于3000万，市值小于300亿，{coordinates_date}日竞价涨停的除外，{coordinates_date}日竞价跌停的也不要，非st，{excoordinates_date}日未涨停也未曾涨停')['股票代码'].tolist()
        stock_list.extend(stock_list1)
        return stock_list
    stock_list = get_ths_stock(excoordinates_date, coordinates_date)
    list2=[name_suffix_transition(i) for i in stock_list]
    print(list2)
    return list_intersection(list1, list2)
print(ths_kpl('2024-05-07','2024-05-08'))

