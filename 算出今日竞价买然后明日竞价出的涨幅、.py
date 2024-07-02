from crazy import *
dataframe_completely_display()
today = datetime.date.today()
today_str = today.strftime("%Y%m%d")  # 获得今日日期
date_list = get_transaction_date(20240101, today_str)
print(date_list)
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
print(get_today_price_minus_yes_price(300283,'20240627'))