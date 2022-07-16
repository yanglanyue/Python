"""
    P367【第19天】（加QQ：2250307122领取配套源码资料）
    拓展dict

"""

class A(object):

    # 类属性
    a = 10

    def __init__(self):
        # 实例属性
        self.b = 500

aa = A()
# 用类调用 __dict__ 会以字典形式返回类中所有定义的的函数和属性
print(A.__dict__)
# 用实例对象调用 __dict__ 会以字典形式返当前对象的实例属性
print(aa.__dict__)



