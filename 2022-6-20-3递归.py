"""
    P221【第12天】（加QQ：2250307122领取配套源码资料）
    递归:
    函数内部自己调用自己
    必须由出口

"""
# 实现数字累加，不同计算机最大递归次数不同，Mac_mini是995

def num_plus(x):
    if x == 1:
        return 1
    else:
        return x + num_plus(x - 1)

x = int(input('输入累加到哪个数：'))
print(num_plus(x))








