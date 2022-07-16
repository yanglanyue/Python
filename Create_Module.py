"""
    P338【第18天】（加QQ：2250307122领取配套源码资料）
    制作模块

"""
def plus_fun(a,b):
    print(f'{a} + {b} = {a + b}')

# 测试信息要么删掉，要么加入 if __name__ == '__main__':
# 意为调用这个方法的是模块自身才执行这个测试方法
# 每一个模块在自己内部看来 __name__ 都是 __main__ ，只有外部导入此模块时此模块的 __name__ 才是模块的文件名
if __name__ == '__main__':
    plus_fun(5,6)

__all__ = ['A','B']

def A():
    print('A方法')

def B():
    print('B方法')

def C():
    print('C方法')


