"""
input
"""

# name = input('请输入姓名：')
# print(f'你的名字：{name}\n输入的数据类型是：{type(name)}')


"""
转换数据类型的函数
int(x[,base])	将X转换为一个整数
float(x)	将X转换为一个浮点数
complex(real[,imag])	创建一个复数，real为实部，imag为虚部
str(x)	将对象x转换为字符串
repr(x)	将对象x转换成表达式字符串
eval(str)	用来计算在字符串中的有效Python表达式，并返回一个对象
tuple(s)	将序列s转换为一个元组
list(s)	将序列s转换为一个列表
chr(x)	将一个整数转换为一个Unicode字符
ord(x)	将一个字符串转换为它的ASCII整数值
hex(x)	将一个整数转换为一个十六进制字符串
oct(x)	将一个整数x转换为一个八进制的字符串
"""

X = input('请输入数据：')
print(f'输入的数据类型：{type(X)}')

X0 = int(X)
print(f'转换之后的数据类型：{type(X0)}')

X1 = str(X0)
print(f'转换之后的数据类型：{type(X1)}')

# 列表转换成元组
list1 = [10,20,30,40]
print(tuple(list1))

# 元组转换成列表
t1 = (100,200,300,400)
print(list(t1))

# eval()将字符串中的数据转换成它原本的数据类型。（计算字符串中的有效的表达式，并返回一个对象）
str1 = '1'
str2 = '1.5'
str3 = '[10,20,30,40]'
str4 = '(100,200,300,400)'
print(eval(str1))
print(type(eval(str1)))
print(eval(str2))
print(type(eval(str2)))
print(eval(str3))
print(type(eval(str3)))
print(eval(str4))
print(type(eval(str4)))








