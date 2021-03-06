"""
    P143【第7天】
    集合
    创建集合使用{}或set()
    创建空集合只能使用set()，因为{}是用来创建空字典的

    集合存储数据是无序的，无法用下标操作
    集合内数据不能从复，集合具有去重功能

"""
# 创建集合
s1 = {0,1,2,3,4,5,6,7,8,9,'A','B','C','G','Tom'}
# 创建空集合
s2 = set()
print(f'集合s1：{s1}')
# 集合中是字符串将被筛分
s3 = set('ABCDEFG')
print(f'用set()创建的集合s3中的字符串将被筛分成：{s3}')


"""
    P144【第7天】
    增
    
    add()
    增加单一数据
    
    update()
    增加数据序列

"""
s4 = {0,1,2,3,4,5,6,7,8,9,'A','B','C'}
# add()增加单一数据，集合具有去重功能，若增加相同数据将覆盖原有数据，系统不会报错
s4.add(100)
print(f'add增加单一数据到集合s4：{s4}')

# update()增加数据序列
s4.update(['1A','KS','G88'])
# 若不以序列增加，所有元素会被彻底拆分成单个元素在进行添加
s4.update('2A','KSM','G99')
print(f'update增加数据序列到集合s4：{s4}')
# 不能添加int类型，int类型不支持迭代
# s4.update(12345)
print(f'update增加数据序列到集合s4：{s4}')


"""
    P145【第7天】
    删

    remove()
    删除集合中的指定数据，如果数据不存在则报错

    discard()
    删除集合中的指定数据，如果数据不存在则不会报错
    
    pop()
    随机删除某个数据并返回这个数据

"""
s5 = {0,1,2,3,4,5,6,7,8,9,'A','B','C'}

# remove()
s5.remove(0)
print(f'remove方法删除集合s5中数据：{s5}')
# discard()
s5.discard('G')
print(f'discard方法删除集合s5中数据：{s5}')
# pop()
p1 = s5.pop()
print(f'pop方法删除集合s5中数据：{s5}，被删除的数据：{p1}')


"""
    P146【第7天】
    查

    in
    判断数据在集合序列

    not in
    判断数据不在集合序列

"""

s6 = {0,1,2,3,4,5,6,7,8,9,'A','B','C'}
print(1 in s6)
print(1 not in s6)



