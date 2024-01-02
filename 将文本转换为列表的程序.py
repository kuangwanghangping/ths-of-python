text = """板块名称		

人民币贬值受益	

阿里巴巴概念	

电机		


"""

list1 = [item.strip() for item in text.split('\n') if item.strip() != '']
print(list1)