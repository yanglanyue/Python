"""
    P157【第8天】（加QQ：2250307122领取配套源码资料）
    推导式

    列表推导式
    用一个表达式创建一个有规律的列表或控制一个有规律的列表
    格式：[xx for xx in range()]

    字典推导式
    快速合并列表
    格式：[xx:yy for xx,yy in ...]

    P166【第8天】
    集合推导式
    格式：[xx for xx in ...]

"""
# 列表推导式
list1 = []

# 传统for循环写法写法
for i in range(10):
    list1.append(i)
print(list1)

# 列表推导式写法
list2 = [i for i in range(10)]
print(list2)

# 带if的列表推导式写法，求50以内能够被3整除的整数
list2 = [i for i in range(50) if i % 3 == 0]
print(list2)
# 列表推导式for循环嵌套
list3 = [(i,j,k,l) for i in range(0,2) for j in range(0,2) for k in range(0,2) for l in range(0,2)]
print(list3)

# 字典推导式
# value是key的平方的字典
# i = 1
dict1 = {i: i**2 for i in range(10)}
print(f'字典推导式输出value是key的平方：{dict1}')

# 将两个列表合并为一个字典
listA = ['name','age','sex']
listB = ['Tom',25,'男']
dict2 ={listA[i]:listB[i] for i in range(len(listA))}
print(dict2)
# 传统for循环方法
dict3 = {}
for i in range(len(listA)):
    dict3[listA[i]] = listB[i]
print(dict3)

# 提取字典中目标数据
# 提取数量大于某个值的电脑品牌
countA = {'Macbook':56,'SONY':20,'DELL':133,'HP':98,'ASUS':167,'Lenovo':144}
x = int(input('输入销量数字：'))

for i,j in countA.items():
    if j >= x:
        print(f'{i}',end=' ')
print()
# 字典推导式
count_a = {i:j for i,j in countA.items() if j >= x}
print(count_a.keys())
print(count_a.items()) #返回的迭代器里面是元组


# 集合推导式，P166【第8天】
# 创建一个集合，数据为下方列表的平方
list_a = [1,2,3,4,5]

set_a = {i**2 for i in list_a}
print(set_a)





