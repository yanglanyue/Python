"""
    格式化输出
    %c	字符
    %s	通过str() 字符串转换来格式化
    %i	有符号十进制整数
    %d	有符号十进制整数
    %u	无符号十进制整数
    %o	八进制整数
    %x	十六进制整数（小写字母）
    %X	十六进制整数（大写字母）
    %e	索引符号（小写'e'）
    %E	索引符号（大写“E”）
    %f	浮点实数
    %g	％f和％e 的简写
    %G	％f和％E的简写
"""

age = 18
name = 'Tom'
weight = 75.5
stu_id1 = 15
stu_id2 = 1895

print('我的年龄是%d岁' % age)

print('我的名字叫%s' %name)

print('我的体重是%fKG' %weight)
# %f之间加入“.数字”表示精确到小数点后面的位数
print('我的体重是%.1fKG' %weight)

print('我的学号是%d号' %stu_id1)
# %d之间加入“0数字”表示按标示的数字输出位数，前面用0补齐，多余的则按原样输出
print('我的学号是%03d号' %stu_id2)

# 连续输出多个数据
print('我的名字叫%s，我的年龄是%d岁，学号是%03d' % (name,age,stu_id1))
# 用%s连续输出多个数据
print('我的名字叫%s，我的年龄是%s岁，体重是%sKG，学号是%s' % (name,age,weight,stu_id1))

# 用f连续输出多个数据（Python 3.6中新增的格式化方法，更简单易读）
print(f'我的名字叫{name}，我的年龄是{age}岁，体重是{weight}KG，学号是{stu_id1}')
# \n换行和\t制表符（一个tab键）
print(f'\t我的名字叫{name}，我的年龄是{age}岁\n\t体重是{weight}KG，学号是{stu_id1}')

# print输出结束系统默认是\n作为结束符，所以可以手动改写print输出的结束符
print('我的名字叫%s' %name, end='...')
print('我的名字叫%s' %name, end='\n')











