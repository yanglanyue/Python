"""
    P226【第12天】（加QQ：2250307122领取配套源码资料）
    lambda表达式（匿名函数）
    格式：
    lambda 参数列表:表达式
    参数可有可无，只能返回一个表达式的值

"""
# 函数
def fn1():
    return 200

print(fn1)
print(fn1())

# lambda表达式（无参数）
fn2 = lambda:100

print(fn2)
print(fn2())

# ======================================================================================================================
# def print_info(int1,int2):
#     print(f'{int1}的{int2}次方是：{int1**int2}')
#
# int1 = int(input('请输入要计算的数字：'))
# int2 = int(input('计算几次方？：'))
# print_info(int1,int2)

# lambda表达式
print_info_l = lambda int3,int4 : print(f'{int3}的{int4}次方是：{int3**int4}')
int3 = int(input('请输入要计算的数字：'))
int4 = int(input('计算几次方？：'))
print_info_l(int3,int4)


# 一个参数
fn3 = lambda a:a
print(fn3('hello python'))

# 默认参数
fn4 = lambda a,b,c=100 : a + b + c
print(fn4(10,20))

# 可变参数：*args，返回一个元组
fn5 = lambda *args : args
print(fn5(1,2,3))
print(fn5(10,20,30,40))
print(fn5(100,200,300,400,500))

# 可变参数：**kwargs，返回一个字典
fn6 = lambda **kwargs : kwargs
print(fn6(a=100,b=200,c=300,d=400))
print(fn6(b=700,a=22,c=333))

# ======================================================================================================================P234【第12天】 lambda的应用
fn_1 = lambda a,b : a if a > b else b
print(fn_1(500,400))


# 将列表中每个字典按字典里age的大小顺序从新进行列表排序
list_l = [
    {'name':'Tom','sex':'男','age':28},
    {'name':'Jack','sex':'男','age':32},
    {'name':'Lucy','sex':'女','age':18},
    {'name':'Lily','sex':'女','age':33},
    {'name':'Elon','sex':'男','age':27}
]
# 升序
list_l.sort(key=lambda x:x['age'])
for i in list_l:
    print(i)
# 降序
list_l.sort(key=lambda x:x['age'],reverse=True)
for i in list_l:
    print(i)





