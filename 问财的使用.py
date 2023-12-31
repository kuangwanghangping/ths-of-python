import pywencai
from crazy import *
dataframe_completely_display()
res = pywencai.get(query = '股票概念',loop=True)
dict1 = dict(zip(res['股票代码'],res['所属概念']))

print(dict1)