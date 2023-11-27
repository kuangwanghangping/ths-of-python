dict = {'节能国祯': ['国企改革', '地方国企改革', '节能环保', '新型城镇化', '央企国企改革'], '蓝天燃气': ['平安资管持股', '沪股通', '天然气管道', 'LNG加气站', '天然气']}
n = ['天然气', '平安资管持股']
def reserve_dict_list_list (dict77,list20):
    result = {k: [v for v in dict77[k] if v in list20] for k in dict77}
    return result
def del_dict_list_list(dict27,list32):
    result43 = {k: [v for v in dict27[k] if v not in list32] for k in dict27}
    return result43
print(reserve_dict_list_list(dict,n))
print(del_dict_list_list(dict,n))

