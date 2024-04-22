import json
import requests

def get_data():
    url = 'https://apphis.longhuvip.com/w1/api/index.php'
    headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N976N Build/QP1A.190711.020)'}
    datas = {
        'ZSType': '7',
        'VerSion': '5.14.0.0',
        'Type': '1',
        'st': '71',
        'RStart': '0925',
        'REnd': '0930',
        'PhoneOSNew': '1',
        'Order': '1',
        'Index': '0',
        'DeviceID': 'ffffffff-d151-c2cd-0000-00002cd5753b',
        'Date': '2024-04-19',
        'c': 'ZhiShuRanking',
        'apiv': 'w36',
        'a': 'RealRankingInfo'
    }
    response = requests.post(url, data=datas, headers=headers)
    response.encoding = response.apparent_encoding
    data = json.loads(response.text)
    print(data['list'])

if __name__ == '__main__':
    get_data()
