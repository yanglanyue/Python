"""
    P266【第14天】（加QQ：2250307122领取配套源码资料）
    面向对象

"""
class Washer():


    def wash(self): # self指的就是调用该函数的对象
        print('洗衣服')
        print(f'类里面获取：{self.weigth}')

SAMSUNG = Washer()
# 在类外面添加对象属性
SAMSUNG.weigth = 500
SAMSUNG.wash()
print(SAMSUNG.weigth)

LG = Washer()
# 在类外面添加对象属性
LG.weigth = 700
LG.wash()
print(LG.weigth)

# ====================================================================================================================== P275【第14天】 魔法方法 __xx__()
# __init__()：初始化对象，在创建对象时自动被调用，不需要手动调用
class Telephone():

    def __init__(self):
        self.brand = 'iphone'
        self.model = '13 Pro Max'

    def print_info(self):
        print(f'品牌：{self.brand}')
        print(f'型号：{self.model}')

ph_1 = Telephone()
ph_1.print_info()

# ====================================================================================================================== P276【第14天】 带参数的__init__()
# ====================================================================================================================== P277【第14天】 魔法方法__str__()
# ====================================================================================================================== P278【第14天】 魔法方法__del__()
class Telephone():

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def __str__(self): # 通常打印对象会打印对象所在的内存地址，加入__str__()方法后，打印对象将会返回这个方法return的数据
        return '这是一个手机对象'

    def __del__(self): # 程序运行完之后计算机会自动释放内存，也就是程序运行结束之后会自动调用__del__方法
        print(f'{self}对象已被删除')

    def print_info(self):
        print(f'品牌：{self.brand}')
        print(f'型号：{self.model}')

ph_2 = Telephone('SAMSUNG','22 Ultra')
ph_2.print_info()
print(ph_2)

ph_3 = Telephone('xiaomi','MIX 6')
ph_3.print_info()
print(ph_3)












