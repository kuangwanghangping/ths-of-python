from crazy import *

print(get_all_bonds('historical'))
res = pywencai.get(query = '今日涨停的股票,',loop=True)
res = res['xuangu_tableV1']
def add_suffix(code):
    if code.startswith('6'):
        return code + '.SH'
    elif code.startswith('0'):
        return code + '.SZ'
    else:
        return code + '.BJ'
res['code'] = res['code'].apply(add_suffix)
upstops_stock = res['code'].tolist()
print(upstops_stock)
that_day_stock_upstops_bond = []
for i,ii in get_all_bonds('historical').items():
    for n in upstops_stock:
        if ii == n :
            that_day_stock_upstops_bond.append(i)
print(that_day_stock_upstops_bond)



