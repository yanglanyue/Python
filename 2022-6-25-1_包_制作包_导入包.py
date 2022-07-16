"""
    P347【第18天】（加QQ：2250307122领取配套源码资料）
    包

    制作包

    导入包

    在包中的 __init__.py文件中添加 __all__ = [] ，控制允许导入的模块列表

"""
# 导入包【方法 1 】导入整个包对应的模块
import package_test.test_00
package_test.test_00.plus_fun(67,21)

# 导入包【方法 2 】导入包对应的模块，这种方法必须配合包中的 __init__.py 文件中添加 __all__ = [] ，控制调用权限
# 以下写法有问题
# from package_test.test_01 import *
# test_01

# 应该按以下写法调用
from package_test import *
test_01.A_01()





