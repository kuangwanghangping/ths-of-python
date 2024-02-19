from crazy import *
dataframe_completely_display()

def get_redeem_remain_days_equal_1():
    jsl_neirong = crawler_inactivity_web('https://www.jisilu.cn/webapi/cb/redeem/')['data']
    for i in jsl_neirong:
        if i['redeem_remain_days'] == 1:
            return i['bond_id']
    #print(get_redeem_remain_days_equal_1())这个是得到最后一天要宣布强赎与否的票，就是不隔夜
    #113063
if __name__ == '__main__':
    print(get_redeem_remain_days_equal_1())


