"""
字符串
"""
# 字符串的几种写法
strA = 'abcd'
strB = "abcd"
strC = '''ab
cd'''
strD = """absadk12
    ahfjacd"""

strE = "I'm Tom"
strF = 'I\'m Tom'

print(strF)

"""
下标:截取其中某个数据
"""
print(strD[2])
print(strD[4])

"""
切片：截取其中磨一段数据，一定注意起点和终点决定了切片的方向！方向！方向！再由步长的正负确定取值的方向！
序列[开始位置下标（包含开始位置数据）:结束位置下标（但不包含结束位置数据）:步长（也就是间隔，也是取数据的方向，可正向（+）也可反向（-），默认值是1）]
"""
strG = "Hello,I'm Tom!How are you?"
print(strG[3:18:2])
strH = '0123456789'
print(strH[0:5:1])
print(strH[:9])
print(strH[:])
# 负数测试
print(f'负数测试{strH[::-1]}')
print(strH[-1:-5:-1])
print(strH[-5:-1:1])


"""
    字符串的查找
    find：不存在返回-1
    rfand：右边开始查找
    index：不存在会报错
    rindex：右边开始查找
    count：查找元素的个数
"""

strX = "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks."
print(strX)
print(strX.find('0'))
print(strX.find('a',31))
print(strX.rfind('a',11,))
print(strX.find('0',19))
print(strX.find('X'))
print(strX.rfind('0',11,))

print(strX.index('0'))

print(strX.count('e'))

"""
    字符串的修改
    替换
    repla()
    格式：字符串.replace('要修改内容','修改后内容',替换的次数)
    
    分割
    split()
    按照指定字符分割字符串，返回一个列表，会丢失用以分割的数据。
    格式：
    字符串.split('用以分割的字符或子串',从左往右需要分割的次数)
    
    合并
    join()：用一个字符或子串合并字符串，即是将多个字符串合并为一个新的字符串
    
    将字符串第一个字符转换成大写
    capitalize()
    
    将字符串每个单词第一个字符转换成大写
    title()
    
    将字符串中每一个字符转换成小写
    lower()
    
    将字符串中每一个字符转换成大写
    upper()
    
    删除字符串左侧空白字符
    lstrip()
    
    删除字符串右侧空白字符
    rstrip()
    
    删除字符串两侧空白字符
    strip()
"""
print(strX)
print(strX.replace('2009','2022'))

# split()：按照指定字符分割字符串，返回一个列表，会丢失用以分割的数据
print(strX.split('e',2))

# join()：用一个字符或子串合并字符串，即是将多个字符串合并为一个新的字符串
listA = ['我','是','你','爸','爸','的','爷爷']
print('xxx'.join(listA))

# 将字符串第一个字符转换成大写
print(strX.capitalize())

# 将字符串每个单词第一个字符转换成大写
print(strX.capitalize().title())

# 将字符串中每一个字符转换成小写
print(strX.capitalize().title().lower())

# 将字符串中每一个字符转换成大写
print(strX.capitalize().title().lower().upper())

# 删除字符串左、右、两侧空白字符
strXX = '   ABCDEFG   '
print(strXX.lstrip())
print(strXX.rstrip())
print(strXX.strip())



"""
    填充字符串
    ljust()
    格式：
    ljust(要扩充的字符串到什么长度,'以什么填充')
    ...
"""
strXXX = 'AAABBB'
print(strXXX.ljust(10,'+'))
print(strXXX.rjust(10,'#'))
print(strXXX.center(20,'*'))

"""
    判断字符串是否以指定子串开头
    startswith()
    格式：
    字符串序列.startswith(子串,开始位置下标,结束位置下标)
    
    endswith()
    格式：
    字符串序列.endswith(子串,开始位置下标,结束位置下标)
"""
print(strX.startswith('Th',0,20))
print(strXXX.startswith('f'))
# endswith()
print(strX.endswith('banks'))
print(strXXX.endswith('ABB',2,5))


"""
    判断字符串中是否都是字母(没有空格)
    isalpha()
    格式：
    字符串序列.isalpha()
    
    判断字符串中是否都是数字(没有空格)
    isdigit()
    格式：
    字符串序列.isdigit()
    
    判断字符串中是否都是数字和字母(没有空格)
    isalnum()
    格式：
    字符串序列.isalnum()
    
    判断字符串中是否都是空白
    isspace()
    格式：
    字符串序列.isspace()
"""
strT = 'AAABBBCCC123'
print(strT.isalpha())
print(strT.isdigit())
print(strT.isalnum())
print(strT.isspace())










