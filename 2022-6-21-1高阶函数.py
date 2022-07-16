"""
    P236【第12天】（加QQ：2250307122领取配套源码资料）
    高阶函数

"""
# abs()：求绝对值函数
print(abs(-10))

# round()：四舍五入函数
print(round(1.5))
print(round(5.1))

# 高阶函数结合lambda表达式的应用，abs或round函数作为参数传入函数
fn1 = lambda a,b,c : c(a) + c(b)
print(fn1(-100,-5,abs))

fn2 = lambda a,b,c : c(a) + c(b)
print(fn2(1.06,4.6,round))

# ======================================================================================================================P240【第12天】 内置高阶函数
# map()
# 格式：map(func,lst)，将传入的函数变量 func 作用到 lst 变量的每个元素中，并将结果组成新的列表（Python2）/迭代器（Python3）返回

# 完成list_1列表中元素的二次方
list_1 = [1,2,3,4,5,6]

def fumc_1(x):
    return x ** 2

print(map(fumc_1,list_1)) # 打印所在内存地址
print(list(map(fumc_1,list_1)))

# reduce()
# 格式：reduce(func,lst)，func必须有两个参数。每次 func 计算的结果继续和序列的下一个元素做累积计算
# 计算列表中数据的累加
import functools

p_1 = int(input('输入起始值：'))
p_2 = int(input('输入结束值：'))
list_2 = []

while p_1 <= p_2:
    list_2.append(p_1)
    p_1 += 1

print(f'列表：{list_2}')

def fun_2(a,b):
    return a + b

print(f'累加计算结果：{functools.reduce(fun_2,list_2)}')

# filter()
# 格式：filter(func,lst)，用于过滤序列，过滤掉不符合条件的元素，返回一个 filter 对象。如果要转换为列表，可以使用 list() 来转换
# 过滤出列表中能被2整除的数字
p_3 = int(input('输入整除的数字：'))

def fun_3(a):
    return a % p_3 == 0

print(f'所在内存中的地址：{filter(fun_3,list_2)}')
print(f'其中能被 {p_3} 整除的数字：{list(filter(fun_3,list_2))}')






