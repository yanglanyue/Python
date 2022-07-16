"""
    P156【第8天】（加QQ：2250307122领取配套源码资料）
    容器类型转换

    tuple()

    list()

    set()

"""
list1 = ['A','B','C','D']
set1 = {0,1,2,3,4,5,6,7,8,9,'A','B','C','G','Tom'}
tuple1 = ('XX','YY','ZZ')

print(type(tuple(list1)))
print(type(tuple(set1)))

print(type(list(tuple1)))
print(type(list(set1)))

print(type(set(tuple1)))
print(type(set(list1)))




