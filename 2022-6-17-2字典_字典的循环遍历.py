"""
    P133【第7天】
    字典

"""
# 有数据字典
dict1 = {'name':'Tom','sex':'男','age':20}
print(dict1)
print(type(dict1))

# 创建空字典
dict2 = {}
dict3 = dict()
print(type(dict3))

"""
    P134【第7天】
    增
"""
dict1['ID'] = 99
dict1['name'] = 'Lucy'
print(dict1)


"""
    P135【第7天】
    删
    del()
    
    请空
    clear()
"""
# 删除整个字典
# del(dict1)

# 删除字典中的键值对
del dict1['name']
print(f'删除dict1后：{dict1}')

dict1.clear()
print(f'请空dict1后：{dict1}')


"""
    P136【第7天】
    改
"""
dict1['name'] = 'Eve'
print(f'修改dict1的name后：{dict1}')


"""
    P137【第7天】
    查
    
    函数查找
    get()
    
    keys()
    
    values()
    
    items()
    
"""
# 键要输对，无效键将会报错
print(dict1['name'])

dict3 = {'name':'Jack','sex':'男','age':20}

# get函数
print(dict3.get('name'))
print(dict3.get('QQ',1234567)) #返回输入的value
print(dict3.get('IG')) #返回None
print(dict3)

# 查找字典中所有的key，返回可迭代对象
print(dict3.keys())

# 查找字典中所有的value，返回可迭代对象
print(dict3.values())

# 查找字典中所有的键值对，返回可迭代对象，里面的数据是元组，元组数据1是key，元组数据2是value
print(dict3.items())


"""
    P138【第7天】
    字典的循环遍历
    
    keys()
    遍历字典的键
    
    values()
    遍历字典的值
    
    items()
    遍历字典的元素
    
    key,value
    遍历字典的键值对
"""

dict4 = {'name':'Elon','sex':'男','age':48,'ID':888000}

# 遍历字典的键
for key in dict4.keys():
    print(f'循环遍历dict4的key：{key}')
# 遍历字典的值
for value in dict4.values():
    print(f'循环遍历dict4的value：{value}')
# 遍历字典的元素
for item in dict4.items():
    print(f'循环遍历dict4的item：{item}')
# 遍历字典的键值对
for key,value in dict4.items():
    print(f'循环遍历dict4的key,value：')
    print(f'{key}：{value}')





