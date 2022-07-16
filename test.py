# a = 0
# while a < 10:
#     if a == 5:
#         print('OK')
#         a += 1
#         continue
#     print('ABCDEFG')
#     a += 1
# else:
#     print('OVER')

# f = open('test.txt','a+')
#
# f.seek(17,0)
#
# print(f.read())
#
# f.close()

# def save():
#     global old_name
#     global index
#     old_name = input('输入要备份的文件名：')
#     index = old_name.rfind('.')
#     return index
#
# if save() > 0:
#     postfix = old_name[index:]
#     new_name = old_name[0:index] + '[备份]' + postfix
#     print(f'备份为：{new_name}')
#
#     old_f = open(old_name, 'rb')
#     new_f = open(new_name, 'wb')
#
#     while True:
#         con = old_f.read(1024)
#         if len(con) == 0:
#             break
#         new_f.write(con)
#
#     old_f.close()
#     new_f.close()
# else:
#     save()

# coding: utf-8

# 创建一个类，类名称第一个字母大写,可以带括号也可以不带括号

# class Student():
#     student_count = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.age = salary
#         Student.student_count += 1
#
#     def display_count(self):
#         print('Total student {}'.format(Student.student_count))
#
#     def display_student(self):
#         print('Name: {}, age: {}'.format(self.name, self.age))
#
#     def get_class(self):
#         if self.age >= 7 and self.age < 8:
#             return 1
#         if self.age >= 8 and self.age < 9:
#             return 2
#         if self.age >= 9 and self.age < 10:
#             return 3
#         if self.age >= 10 and self.age < 11:
#             return 4
#         else:
#             return 0
#
#
# # 创建类的对象（实例化类）
# # python中实例化类不需要使用关键字new（也没有这个关键字），类的实例化类似函数调用方式。
#
# student1 = Student('cuiyongyuan', 10)
# student2 = Student('yuanli', 30)
#
# student1.display_student()
# student2.display_student()
#
# student1_class = student1.get_class()
# student2_class = student2.get_class()
# print(student1_class)
# print(student2_class)

# import random
#
# print(random.randint(1,3))


import os
# 获取目录列表
print(os.listdir()) # 获取当前目录下列表
print(os.listdir('Personnel_management_system'))

os.chdir('F:\Beautyleg')
print(os.listdir(os.chdir('F:\Beautyleg')))




