"""
    P148【第8天】（加QQ：2250307122领取配套源码资料）
    公共操作

    +
    合并（字符串、列表、元组）

    *
    复制（字符串、列表、元组）

    in
    元素是否存在（字符串、列表、元组、字典）

    not in
    元素是否不存在（字符串、列表、元组、字典）

"""

str1 = 'hello Python'
str2 = '0123456789'

list1 = ['A','B','C','D']
list2 = [0,1,2,3,4,5,6,'aa','bb','cc']

tuple1 = (0,1,2,3)
tuple2 = ('XX','YY','ZZ')

dict1 = {'name':'Tom','age':25,'sex':'男','ID':9988}
dict2 = {'name':'Lucy','age':22,'sex':'女'}

# +：合并
print(str1 + str2)
print(list1 + list2)
print(tuple1 + tuple2)
# 字典不支持合并运算
# print(dict1 + dict2)

# *：复制
print(str1 * 3)
print(list1 * 3)
print(tuple1 * 3)
# print(dict1 * dict2)

# in/not in：元素是否存在
print('h' in str1)
print('x' in list1)
print('YY' not in tuple2)
print(22 in dict2.values())
print('name' not in dict1.keys())


"""
    P151【第8天】（加QQ：2250307122领取配套源码资料）
    公共方法

    len
    查看长度（字符串、列表、元组、字典）
    
    P152【第8天】
    del或者del()
    删除
    
    max()
    求最大值
    
    min()
    求最小值

"""
print('len方法查看长度')
# len查看长度
print(len(str1))
print(len(list1))
print(len(tuple1))
print(len(dict2))

print('del或者del()删除操作')
# del或者del()
# del str1
# print(str1)

del(list1[0])
print(list1)

# del tuple1
# print(tuple1)

del dict2['name']
print(dict2)

print('max求最大值')
# max求最大值
print(max(str1))
print(min(str1))
print(max(tuple2))
print(max(dict1))

"""
    P154【第8天】（加QQ：2250307122领取配套源码资料）
    公共方法

    range(start,end,step)
    生成从start到end的数字，步长为step，供for循环使用
    类似字符串中的切片，包含start位，不包含end位
"""
# 直接打印range(0,10,1)会返回这个可迭代的对象
print(range(0,10,1))

for i in range(0,10,1):
    print(i,end=' ')
print()

for i in range(0,10,2):
    print(i,end=' ')
print()

# 只写一个数字代表结尾，开始默认为0，步长默认为1
for i in range(10):
    print(i,end=' ')
print()

"""
    P155【第8天】（加QQ：2250307122领取配套源码资料）
    公共方法

    enumerate()
    enumerate(可遍历对象,start=0)
    
"""
# 返回元组：(下标,下标对应的数据)
for i in enumerate(list2):
    print(i,end=' ')
print()

# start = 数字，更改返回元组下标起始值
for i in enumerate(list2,start = 1):
    print(i,end=' ')

