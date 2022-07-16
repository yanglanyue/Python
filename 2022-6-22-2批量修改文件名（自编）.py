import os

src = input('输入文件夹路径：')
list_f = os.listdir(src)
for i in list_f:
    print(i)

os.chdir(src)
print(f'总计 {len(list_f)} 个文件')

postfix = input('输入要修改成的文件后缀名：')
for i in list_f:
    j = 0
    if i[i.rfind('.'):] == '.png' or i[i.rfind('.'):] == '.webp' or i[i.rfind('.'):] == '.jfif' or i[i.rfind('.'):] == '.jpeg' or i[i.rfind('.'):] == '.jpg!d' or i[i.rfind('.'):] == '.jpg!aqp':
        if i[:i.rfind('.')] + '.' + postfix in list_f:
            # 此处 if 内部的 if判断是识别文件夹内是否有同名但后缀不同的文件，若有同名仅仅是后缀不一样的文件则会新建一个将要修改成的同名在文件名尾部加上“（整数）”以区分修改文件后文件名和后缀都相同的问题
            # 以下 '(%d).'%j 中的 '(%d).' 是指添加一个括号和括号中添加数据， %d 为无符号十进制整数的格式化输出，而 %j 也是格式化输出的课程内容，j 是已经定义的整数 0 ，后面会实现自增
            new_name = i[:i.rfind('.')] + '(%d).'%j + postfix
            print(f'备份为：{new_name}')

            old_f = open(i, 'rb')
            new_f = open(new_name, 'wb')

            while True:
                con = old_f.read(1024)
                if len(con) == 0:
                    break
                new_f.write(con)

            old_f.close()
            new_f.close()
            os.remove(i)
            j += 1
        else:
            new_name = i[:i.rfind('.')] + '.' + postfix
            os.rename(i,new_name)


