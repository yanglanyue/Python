"""
循环相关
"""

a = 0

while a <= 10:
    print(a, end='')
    a += 1
print()

"""
while循环
计数器控制累加的两种写法
"""
x = 0
all = 0
while x <= 100:
    all += x
    x += 2 #计数器
print(all, end='')
print()

x = 0
all1 = 0
while x <= 100:
    if x % 2 == 0:
        all1 += x
    x += 2 #计数器
print(all1, end='')
print()

"""
break和continue
break：直接跳出整个循环
continue：跳出这一次循环继续往下循环
"""
import random

ran = random.randint(1,10)
A1 = 1
while A1 <= 10:
    if A1 == ran:
        print(f'break实例，产生的随机数是{A1}')
        break
    print(f'break实例，产生的随机数不是{A1}')
    A1 += 1
print('break实例执行完毕！')

A2 = 1
while A2 <= 10:
    if A2 == ran:
        print(f'continue实例，产生的随机数是{A2}')
        A2 += 1
        continue
    print(f'continue实例，产生的随机数不是{A2}')
    A2 += 1
else:
    print('continue实例执行完毕！')

"""
for循环
"""

str = 'hello dangerous'
for i in str:
    print(f'{i}', end=' ')
print()

# break跳出循环
x1 = input('输入你想截断的字母：')
for i in str:
    if i == x1:
        print(f'你想截断的字母：{i}')
        break
    else:
        print(f'{i}', end='')
print()

# continue跳出循环
x2 = input('输入你想截断的字母：')
for i in str:
    if i == x2:
        print(f'你想截断的字母：{i}')
        continue
    else:
        print(f'{i}', end='')




