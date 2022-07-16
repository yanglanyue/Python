"""
    P263【第13天】（加QQ：2250307122领取配套源码资料）
    批量命名之添加字符串

"""
import os
# 获取当前目录文件列表
# print(os.listdir())

src = input('输入文件夹路径：')
name = input('输入添加字段：')
list_f = os.listdir(src)

for i in list_f:
    if i[:len(name)] != name:
        new_name = name + i
        os.chdir(src)
        os.rename(i,new_name)
    else:
        new_name = i[len(name):]
        os.chdir(src)
        os.rename(i, new_name)









