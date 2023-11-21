import requests
import json
from crazy import *
import pandas as pd
dataframe_completely_display ()
class ths_limitup_data:
    def __init__(self):
        '''
        涨停数据
        '''
    def get_var(self):
        '''
        获取js
        '''
        with open('ths.js') as f:
            comm=f.read()
        comms=execjs.compile(comm)
        result=comms.call('v')
        return result
    def get_headers(self):
        '''
        获取请求头
        '''
        var=self.get_var()
        cookie='Hm_lvt_722143063e4892925903024537075d0d=1694411343; Hm_lvt_929f8b362150b1f77b477230541dbbc2=1694411343; _ga=GA1.1.139385290.1694575911; _ga_KQBDS1VPQF=GS1.1.1694599350.2.0.1694599350.0.0.0; u_ukey=A10702B8689642C6BE607730E11E6E4A; u_uver=1.0.0; u_dpass=Ca4Tyl1S4mcfsTLeJPNBApSK3c4IkiGPLRSOLsO7eH2km3EyrjIp3g4wXKnuDIjF%2FsBAGfA5tlbuzYBqqcUNFA%3D%3D; u_did=276DC66DC3844A1B875166BB3E4039C7; u_ttype=WEB; Hm_lvt_f79b64788a4e377c608617fba4c736e2=1695629642; Hm_lpvt_f79b64788a4e377c608617fba4c736e2=1695629642; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1694411343,1695629642; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1695629642; Hm_lvt_60bad21af9c824a4a0530d5dbf4357ca=1695629642; Hm_lpvt_60bad21af9c824a4a0530d5dbf4357ca=1695629642; v={}'.format(var)
        headers={
            'Cookie':cookie,
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.41'
        }
    def get_limit_up_pool(self,date='20230926'):
        '''
        涨停股票池
        '''
        url='https://data.10jqka.com.cn/dataapi/limit_up/limit_up_pool?'
        params={
            'page': '1',
            'limit': '15000',
            'field': '199112,10,9001,330323,330324,330325,9002,330329,133971,133970,1968584,3475914,9003,9004',
            'filter': 'HS,GEM2STAR',
            'order_field': '330324',
            'order_type': '0',
            'date':f"{date}",
            '_': '1695632712332',
        }
        res=requests.get(url=url,params=params)
        text=res.text
        if len(str(text))<70:
            return False,''
        else:
            try:
                text=res.json()
                df=pd.DataFrame(text['data']['info'])
                df.columns=['开板次数','首次涨停时间','最后涨停时间','证券代码','涨停形态','封单量',
                            '_','最近一年封板率','流通市值','_','_','涨跌幅','换手率','涨停原因',
                            '封单额','几天几板','股票名称','_','_','_','最新价','time_preview']
                del df['_']
                df['封单额比流通市值']=(df['封单额']/df['流通市值'])*100
                def select_daily(x):
                    if x=='首板':
                        return 1
                    else:
                        x=str(x).split('天')[0][-1]
                        return int(x)
                def select_num(x):
                    if x=='首板':
                        return 1
                    else:
                        x=str(x).split('板')[0][-1]
                        return int(x)
                df['几天']=df['几天几板'].apply(select_daily)
                df['几板']=df['几天几板'].apply(select_num)
                return True,df
            except:
                return False,''
    def get_limit_up(self,date='20230925'):
        '''
        冲刺涨停
        '''
        url='https://data.10jqka.com.cn/dataapi/limit_up/limit_up?'
        params={
            'page': '1',
            'limit': '1500',
            'field': '199112,10,48,1968584,19,3475914,9003,9004',
            'filter': 'HS,GEM2STAR',
            'order_field': '199112',
            'order_type': '0',
            'date':f"{date}" ,
            '_': '1695635862890',
        }
        
        res=requests.get(url=url,params=params)
        text=res.text
        if len(str(text))<70:
            return False,''
        else:
            try:
                text=res.json()
                df=pd.DataFrame(text['data']['info'])
                columns=['开板次数','首次涨停时间','最后涨停时间','证券代码','涨停形态','封单量',
                            '_','最近一年封板率','流通市值','_','_','涨跌幅','换手率','涨停原因',
                            '封单额','几天几板','股票名称','_','_','_','最新价','time_preview']
                #del df['_']
                return True,df
            except:
                return False,''
#continuous_limit_pool
    def get_continuous_limit_pool(self,date='20230925'):
        '''
        连扳池
        '''
        url='https://data.10jqka.com.cn/dataapi/limit_up/continuous_limit_pool?'
        params={
            'page': '1',
            'limit': '1500',
            'field': '199112,10,330329,330325,133971,133970,1968584,3475914,3541450,9004',
            'filter': 'HS,GEM2STAR',
            'order_field': '330329',
            'order_type': '0',
            'date': f'{date}',
            '_': '1695696080744',
        }
        res=requests.get(url=url,params=params)
        text=res.text
        if len(str(text))<70:
            return False,''
        else:
            try:
                text=res.json()
                df=pd.DataFrame(text['data']['info'])
                columns=['开板次数','首次涨停时间','最后涨停时间','证券代码','涨停形态','封单量',
                            '_','最近一年封板率','流通市值','_','_','涨跌幅','换手率','涨停原因',
                            '封单额','几天几板','股票名称','_','_','_','最新价','time_preview']
                #del df['_']
                return True,df
            except:
                return False,''
#open_limit_pool?
    def get_open_limit_pool(self,date='20230925'):
            '''
            炸板池
            '''
            url='https://data.10jqka.com.cn/dataapi/limit_up/open_limit_pool?'
            params={
                'page': '1',
                'limit': '15',
                'field': '199112,9002,48,1968584,19,3475914,9003,10,9004',
                'filter': 'HS,GEM2STAR',
                'order_field': '199112',
                'order_type': '0',
                'date':f'{date}',
                '_': '1695696646721',
            }
            res=requests.get(url=url,params=params)
            text=res.text
            if len(str(text))<70:
                return False,''
            else:
                try:
                    text=res.json()
                    df=pd.DataFrame(text['data']['info'])
                    columns=['开板次数','首次涨停时间','最后涨停时间','证券代码','涨停形态','封单量',
                                '_','最近一年封板率','流通市值','_','_','涨跌幅','换手率','涨停原因',
                                '封单额','几天几板','股票名称','_','_','_','最新价','time_preview']
                    #del df['_']
                    return True,df
                except:
                    return False,''
#lower_limit_pool
    def get_lower_limit_pool(self,date='20230925'):
            '''
            跌停
            '''
            url='https://data.10jqka.com.cn/dataapi/limit_up/lower_limit_pool?'
            params={
                'page': '1',
                'limit': '15',
                'field': '199112,10,330333,330334,1968584,3475914,9004',
                'filter': 'HS,GEM2STAR',
                'order_field': '330334',
                'order_type': '0',
                'date': f'{date}',
                '_': '1695697116683',
            }
            res=requests.get(url=url,params=params)
            text=res.text
            if len(str(text))<70:
                return False,''
            else:
                try:
                    text=res.json()
                    df=pd.DataFrame(text['data']['info'])
                    columns=['开板次数','首次涨停时间','最后涨停时间','证券代码','涨停形态','封单量',
                                '_','最近一年封板率','流通市值','_','_','涨跌幅','换手率','涨停原因',
                                '封单额','几天几板','股票名称','_','_','_','最新价','time_preview']
                    #del df['_']
                    return True,df
                except:
                    return False,''
#block_top
    def get_block_top_pool(self,date='20230925'):
            '''
            最强口
            '''
            url='https://data.10jqka.com.cn/dataapi/limit_up/block_top?'
            params={
                'filter': 'HS,GEM2STAR',
                'date':f'{date}'
            }
            res=requests.get(url=url,params=params)
            text=res.text
            if len(str(text))<70:
                return False,''
            else:
                try:
                    text=res.json()
                    df=pd.DataFrame(text['data'])
                    columns=['开板次数','首次涨停时间','最后涨停时间','证券代码','涨停形态','封单量',
                                '_','最近一年封板率','流通市值','_','_','涨跌幅','换手率','涨停原因',
                                '封单额','几天几板','股票名称','_','_','_','最新价','time_preview']
                    #del df['_']
                    return True,df
                except:
                    return False,''
    def read_func_data(self,func="self.get_block_top_pool(date='20230925')"):
        '''
        读取函数数据
        '''
        text=func
        while True:
            stats,df=eval(text)
            if stats==True:
                df=df
                break
            else:
                pass
        return df
    def get_analysis_block_top_pool(self,date='20230925'):
        '''
        解析最强口
        '''
        func="self.get_block_top_pool(date='{}')".format(date)
        df=self.read_func_data(func=func)
        data=pd.DataFrame()
        for code,name,change,limit_up_num ,continuous_plate_num ,high ,high_num ,\
        days,stock_list in zip(df['code'],df['name'],df['change'] ,df['limit_up_num'], df['continuous_plate_num'],
                                df['high'] ,df['high_num'],df['days'],df['stock_list']):
            df1=pd.DataFrame(stock_list)
            df1['行业代码']=code
            df1['name']=name
            df1['change']=change
            df1['limit_up_num']=limit_up_num
            df1['continuous_plate_num']=continuous_plate_num
            df1['high']=high
            df1['high_num']=high_num
            df1['days']=days
            data=pd.concat([data,df1],ignore_index=True)
        data.to_excel(r'数据.xlsx')
        return data
if __name__=='__main__':

    models=ths_limitup_data()
    print(models)
    # dt =models.read_func_data(func="models.get_open_limit_pool(date='20231120')")
    # print(dt)
    #df=models.read_func_data(func="models.get_limit_up_pool(date='20210927')")
   # print(df)

        