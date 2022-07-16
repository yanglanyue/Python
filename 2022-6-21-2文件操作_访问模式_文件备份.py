"""
    P244【第13天】（加QQ：2250307122领取配套源码资料）
    文件操作

    r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
    r+	打开一个文件用于读写。文件指针将会放在文件的开头。
    rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
    w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

"""
# 打开文件
# open(name,mode)

f = open('test.txt','w')

# 写入操作
# write() read()

f.write('ABC')

# 关闭
# close()

f.close()

# ====================================================================================================================== P246【第13天】 访问模式，4 种模式：r w a 无访问模式（默认 r ）
# r：文件不存在会报错；不支持写入，只读；
f = open('test.txt','r')

f.write('AAsssss')

f.close()

# w：如果文件不存在会新建这个文件；执行写入会覆盖原有内容
f = open('test.txt','w')

f.write('aaaaaaaaaa\nbbbbbbbbbb\ncccccccccc\ndddddddddd\neeeeeeeeee')

f.close()

# a：追加
f = open('test.txt','a')

f.write('aaaaaaaaaa\nbbbbbbbbbb\ncccccccccc\ndddddddddd\neeeeeeeeee')

f.close()

# 无访问模式默认 r 访问模式

# ====================================================================================================================== P247【第13天】 读取：read() readlines() readline()
# read(num)：num表示读取文件内部的字节长度
f = open('test.txt','r')
print(f.read(20))
f.close()

# readlines()：按照行的方式把整个文件内容进行一次读取，并且返回一个列表，每一行的数据为一个元素
f = open('test.txt','r')
print(f.readlines())
f.close()

# readline()：调用一次打印一行文件中的内容
f = open('test.txt','r')
print(f.readline())
print(f.readline())
f.close()

# ====================================================================================================================== P251【第13天】
# r+：打开一个文件用于读写。文件指针将会放在文件的开头。（没有文件会报错）
f = open('test.txt','r+')
f.write('12345678900000')
print(f.read())
f.close()

# w+：打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。（没有文件不会报错）
f = open('test.txt','w+')
f.write('123456789')
print(f.read())
f.close()

# a+：打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
f = open('test.txt','a+')
f.write('zzzzzzzzzzz')
print(f.read())
f.close()

# ====================================================================================================================== P252【第13天】 seek()函数
# 格式：文件对象.seek(偏移量,起始位置)
# 0：文件开头
# 1：当前位置
# 2：文件结尾

# 目标 1：改为 r 访问模式的指针读取位置到文件末尾，看是否能读取数据
f = open('test.txt','r+')

f.seek(5,0)

print(f.read())

f.close()

# 目标 2：改为 a 访问模式的指针读取位置到文件开头，看是否能读取数据
f = open('test.txt','a+')

f.seek(5,0)

print(f.read())

f.close()

# ====================================================================================================================== P253【第13天】 文件备份
# 此课题将用到 “2022-6-14字符串” 的学习笔记
# 第 1 步
old_name = input('输入要备份的文件名：')
# 第 2 步，从右边开始查找 “.” 在第几个位置
index = old_name.rfind('.')
# 判断用户输入文件名是否无效
if index > 0:
    postfix = old_name[index:]
# 第 3 步，用到 “2022-6-14字符串” 的学习笔记中字符串切片
new_name = old_name[0:index] + '[备份]' + postfix
print(f'备份为：{new_name}')

# 注意最好用二进制只读访问模式打开
old_f = open(old_name,'rb')
new_f = open(new_name,'wb')

# 循环读取文件源代码
while True:
    con = old_f.read(1024)
    if len(con) == 0:
        break
    new_f.write(con)

old_f.close()
new_f.close()


# ====================================================================================================================== 文件备份改版

def save():
    global old_name
    global index
    old_name = input('输入要备份的文件名：')
    index = old_name.rfind('.')
    return index

if save() > 0:
    postfix = old_name[index:]
    new_name = old_name[0:index] + '[备份]' + postfix
    print(f'备份为：{new_name}')

    old_f = open(old_name, 'rb')
    new_f = open(new_name, 'wb')

    while True:
        con = old_f.read(1024)
        if len(con) == 0:
            break
        new_f.write(con)

    old_f.close()
    new_f.close()
else:
    save()

# ======================================================== P259 ~ P262【第13天】 文件重命名；删除文件；创建文件夹；删除文件夹；获取当前目录；改变默认目录；获取目录列表
# 导入os模块
import os

# 从命名文件或文件夹
os.rename('test_1.txt','test_2.txt')

# 删除文件
os.remove('test_2.txt')

# 创建文件夹
os.mkdir('test_dir')

# 删除文件夹
os.rmdir('test_dir')

# 返回当前文件（这行代码所在的这个 .py文件）所在路径
print(os.getcwd())

# 改变默认目录（从定位到目标文件夹）
os.chdir()
# 示例
# 创建文件夹
os.mkdir('test_dir')
# 切换'test_dir'目录下
os.chdir('test_dir')
# 再创建'test_001'文件夹
os.mkdir('test_001')

import os
# 获取目录列表
print(os.listdir()) # 获取当前目录下列表
print(os.listdir('文件夹名'))









