"""
    P168【第9天】（加QQ：2250307122领取配套源码资料）
    函数

    定义函数
    def 函数名(形参,...):
        代码
        ...

    调用函数
    函数名(实参,...)

"""

def print_info(int1,int2):
    print(f'{int1}的{int2}次方是：{int1**int2}')

int1 = int(input('请输入要计算的数字：'))
int2 = int(input('计算几次方？：'))
print_info(int1,int2)


# 函数中return是退出当前函数，return后面的同级代码不执行
def buy():
    return '方便面'
    print('hello')

goods = buy()
print(goods)


# 函数嵌套调用
def test():
    """测试函数嵌套调用"""
    print('测试调用test函数')

def col1(intA,intB):
    """
    计算输入数字的 n 次方
    :param intA: 要计算 n 次方的数
    :param intB: 要计算几次方
    :return: 返回值
    """
    test()
    return intA**intB

intA = int(input('请输入要计算的数字：'))
intB = int(input('计算几次方？：'))
intC = col1(intA,intB)
print(f'{intA}的{intB}次方是：{intC}')


# help()函数：查看函数说明文档
help(col1)


# 按要求打印图形
str_1 = input('输入需要打印的字符：')
int_1 = int(input('输入需要打印的行数：'))
int_2 = int(input('输入需要打印的列数：'))

def crosswise(str_1,int_1):
    print(f'{str_1}' * int_1)

def go(str_1,int_1,int_2):
    i = 0
    while i < int_2:
        crosswise(str_1,int_1)
        i += 1

go(str_1,int_1,int_2)


"""
    P183【第10天】（加QQ：2250307122领取配套源码资料）
    函数变量作用域
    
    局部变量
    只在函数内生效
    
    全局变量
    函数内外都生效
"""
a = 100

def aa():
    print(a)

# global：将函数内局部变量变成全局变量
def bb():
    global a # 声明 a 为全局变量
    a = 200
    print(a)

aa()
bb()
print(a)

# ====================================================================================================================== P188 【第10天】返回值作为参数传递
def test1():
    return 999

def test2(num):
    print(num)

test2(test1())

# ====================================================================================================================== P189 【第10天】函数的多返回值

def test3():
    # return 1,2,3  # 自动返回一个元组
    # return (1,2,3)    # 返回一个元组
    # return [1, 2, 3]  # 返回一个列表
    # return {1, 2, 3}  # 返回一个集合
    return {'name':'Tom', 'age':25} # 返回一个字典

print(test3())

# ====================================================================================================================== P190~P191 【第10天】函数的参数，关键字参数
# 传入的参数类型、位置、个数要保持一致
def user_inf(name,age,sex):
    print(f'姓名：{name} 年龄：{age} 性别：{sex}')

user_inf('Tom',27,'男')

# 关键字参数，参数位置不存在先后顺序
user_inf(age=32,name='Jack',sex='男')

# ====================================================================================================================== P192 【第10天】缺省参数
# 可以在函数的形参里先定义好默认值，调用函数时若为传入实参，则系统将相应实参设置为形参的默认值
def user_inf(name,age,sex = '不男不女'):
    print(f'姓名：{name} 年龄：{age} 性别：{sex}')

user_inf(age=32,name='Dell')

# ====================================================================================================================== P193 【第10天】不定长参数之位置参数
# 默认形参：*args
def user_inf(*args):
    print(args)

user_inf(32,'Dell','男')

# ====================================================================================================================== P194 【第10天】不定长参数之关键字参数
# 默认形参：**kwargs
def user_inf(**kwargs):
    print(kwargs)

user_inf(age = 32,name = 'Dell',sex = '男')





