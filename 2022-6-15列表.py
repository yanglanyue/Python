"""
列表查找
"""

name_list = ['Tom','Lucy','Lily','Jack','Bob','Rose','Piter','Elon','Bill','Dell','Jobs','William']

# 查找元素下标
print(name_list.index('Elon'))
# 查找列表中某数据出现的次数
print(name_list.count('Lucy'))
# 查找列表中数据长度
print(f'列表原始长度为：{len(name_list)}')


"""
判断列表中元素是否存在
in
not in
"""
print('Dell' in name_list)
print('Dell' not in name_list)

name = input('请输入英文名字：')
n = 0
if name in name_list:
    while name in name_list:
        if name in name_list and n == 0:
            name = input('名字已存在，请从新输入：')
            n =+ 1
        elif name in name_list and n != 1:
            name = input('名字还是存在，请从新输入：')
            n += 1
        else:
            name = input('还是从复！无语！从新输入：')
    print('名字不存在，可以注册')
else:
    print('名字不存在，可以注册')

"""
    增加:
    
    append()
    从列表结尾增加数据，数据也可以是序列（[123, ABC]），将整个序列视作一个元素整体进行添加
    
    extend()
    从列表结尾增加数据，数据也可以是序列（[123, ABC]），将整个序列所有元素彻底拆分成单个最基本元素进行添加
    
    insert()
"""
name_list.append(name)
name_list.extend(['123','ABC'])
name_list.insert(999,'DDD')
print(name_list)
print(f'列表现在长度为：{len(name_list)}')

"""
    删除:
    
    del()
    删除整个列表：del 列表名
    删除指定下标的列表元素：del 列表名[下标]

    pop()
    删除指定下标的列表元素，若不指定将删除列表最后一个数据，并返回被删除的数据

    remove()
    删除指定数据：
    例：remove(数据)
    
    clear()
    请空列表
    
"""
# del name_list[1]
# pop()
a = int(input('你想删除第几个数据：'))
print(f'删除的第{a}个数据是：{name_list.pop(a-1)}')
print(name_list)
print(f'列表现在长度为：{len(name_list)}')
# remove()
b = input('输入你想删除的数据：')
print(f'删除的数据是：{name_list.remove(b)}')
print(name_list)
print(f'列表现在长度为：{len(name_list)}')
# clear()
# name_list.clear()
# print(name_list)
# print(f'列表现在长度为：{len(name_list)}')

"""
    修改:
    
    列表[下标] = "想要修改的数据"

    reverse()
    逆序

    sort()
    排序，升序：reverse = False；降序：reverse = True
    格式：sort(key = None,reverse = False)

"""
c = int(input('想要修改第几个数据：'))
d = input('修改内容为：')
name_list[c-1] = d
print(name_list)
print(f'列表现在长度为：{len(name_list)}')
# reverse()逆序
name_list.reverse()
print(f'逆序后：{name_list}')
# sort()，升序降序
list_A = [1,2,3,4,5,6,7,8,9]
list_A.sort(reverse=True)
print(list_A)

"""
    复制:

    copy()

"""
list_B = list_A.copy()
print(list_B)











