"""
    P333【第17天】（加QQ：2250307122领取配套源码资料）
    模块

    导入模块

    定义别名

    模块定位顺序

    __all__ 列表

"""
# 导入模块【方法 1 】导入整个模块
import dis
import math

import Create_Module
import test
import test_0

print(math.sqrt(101))

# 导入模块【方法 2 】导入模块的某些方法
from math import sqrt,pi,log,pow
print(sqrt(900))
print(log(5))

# 导入模块【方法 3 】导入模块的全部功能
from math import *
sqrt(9)

# ======================================================================================================================  P337【第18天】定义别名，定义别名之后只能使用别名，无法再使用原名
print('================================================ P337【第18天】定义别名，定义别名之后只能使用别名，无法再使用原名')
import math as ma
print(ma.log(6))

import time as tt
tt.sleep(1)

from math import pow as p
print(p(5,3))

import Create_Module as cm
cm.plus_fun(3,6)

# 每一个模块在自己内部看来 __name__ 都是 __main__ ，只有外部导入此模块时此模块的 __name__ 才是模块的文件名
print(cm.__name__)
# 每一个模块在自己内部看来 __name__ 都是 __main__ ，只有外部导入此模块时此模块的 __name__ 才是模块的文件名
print(__name__)

# ======================================================================================================================  P342【第18天】模块定位顺序
# 自定义模块名不能和已有模块名从复，否则无法使用

# 当使用 from 模块 import 方法名 导入方法的时候若遇到多个模块内有方法名相同时将导入最后那个方法
from time import sleep

def sleep(a):
    print(f'由于自身定义了一个与 Time 模块中 sleep 同名的方法，则无法调用 Time 模块中的 sleep 方法，{a}')

sleep(2)

# ======================================================================================================================  P345【第18天】 __all__ 列表
# 模块中含有 __all__ 列表是，使用 from 模块 import * 导入全部方法的时候只能导入 __all__ 列表中的方法
from Create_Module import *
A()
B()
# C()
# plus_fun(5,20)




