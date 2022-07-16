"""
    P355【第19天】（加QQ：2250307122领取配套源码资料）
    创建 management_system 管理系统类

"""
from Person import *
from batch_add import *
import os

class Management_system(object):
    def __init__(self):
        # 存储数据所用列表
        self.person_list = []

# ====================================================================================================================== P357【第19天】
# 定义程序入口函数：加载数据，显示功能菜单，用户输入功能序号，根据用户输入的序号执行相应的功能
# 定义系统功能函数，添加、删除人员等

    # 【1】 程序入口函数
    def run(self):
        # 1 加载人员信息
        # self.load_person()

        while True:
            # 2 显示功能菜单
            self.show_menu()

            # 3 用户输入对应功能的序号【注意输入信息一定要转换成 int 类型，否则系统识别为字符串，if 没有定义字符串的判断，系统将进入死循环！！！】
            # menu_num = int(input('输入功能对应的序号：'))
            menu_num = input('输入功能对应的序号：')

            # 4 执行相应的功能
            if menu_num == '1':
                self.add_person()
            elif menu_num == '2':
                self.del_person()
            elif menu_num == '3':
                self.edit_person()
            elif menu_num == '4':
                self.inquire_person()
            elif menu_num == '5':
                self.show_all_person()
            elif menu_num == '6':
                self.save_person()
            elif menu_num == '7':
                self.load_person()
            elif menu_num == '0':
                break
            else:
                print('输入有误，请从新输入。')


    # 【2】 系统功能函数
    # 显示系统菜单（定义一个静态方法即可）
    @staticmethod
    def show_menu():
        print('========================人员管理系统【选择功能对应序号按回车键】')
        print('1 添加人员')
        print('2 删除人员')
        print('3 修改人员信息')
        print('4 查询人员信息')
        print('5 显示所有人员信息')
        print('6 保存人员信息')
        print('7 打开已有人员信息文件')
        print('0 退出人员管理系统')

    # 添加人员信息 ======================================================================================================= P361【第19天】
    def add_person(self):
        print('【 添加人员信息（姓名，性别，年龄，电话） 】')
        name = input('输入姓名：')
        gender = input('输入性别：')
        age = int(input('输入年龄：'))
        tel = int(input('输入电话：'))

        p = Person(name,gender,age,tel)
        print(f'确认人员信息：【 {p} 】')
        yn = input(f'是否添加 (y/n)：')

        if yn == 'y':
            self.person_list.append(p)
            print('添加成功')
        elif yn == 'n':
            print('没有添加')

    # 删除人员信息 ======================================================================================================= P362【第19天】
    def del_person(self):
        print('【 删除人员信息 】')

        name = input('输入要删除的人员姓名：')

        for i in self.person_list:
            if i.name == name:
                self.person_list.remove(i)
                break
        else: # else之所以不与 if 平级是因为 for 循环会对整个列表挨个遍历，每当遍历一个对象若判断条件不成立则会执行一遍 else ，那如果整个列表所有对象遍历一遍下来条件都不成立则将会执行若干次 else
            print('查不此人')

        # print(self.person_list)
        i = 0
        while i < len(self.person_list):
            print(self.person_list[i])
            i += 1

    # 修改人员信息
    def edit_person(self):
        print('【 修改人员信息 】')

        name = input('输入要修改的人员姓名：')

        for i in self.person_list:
            if i.name == name:
                i.name = input('输入姓名：')
                i.gender = input('输入性别：')
                i.age = int(input('输入年龄：'))
                i.tel = int(input('输入电话：'))
                print('修改成功')
                print(f'姓名：{i.name}   \t性别：{i.gender}   \t年龄：{i.age}   \t电话：{i.tel}')
                break
        else:
            print('查不此人')

    # 查询人员信息
    def inquire_person(self):
        while True:
            print('【 查询人员信息 】')
            print('1 按姓名查询')
            print('2 按性别查询')
            print('3 按年龄查询')
            print('4 按电话查询')
            print('0 返回上级菜单')

            inp = input('输入查询方式对应的序号：')

            if inp == '1':
                name = input('输入要查询人员的姓名：')
                print('人员信息如下')
                j = []
                for i in self.person_list:
                    if i.name == name:
                        print(f'姓名：{i.name}   \t性别：{i.gender}   \t年龄：{i.age}   \t电话：{i.tel}')
                        j.append(i)
                        continue
                if len(j) == 0:
                    print('查无此人')

            elif inp == '2':
                gender = input('输入要查询人员的性别：')
                print('人员信息如下')
                j = []
                for i in self.person_list:
                    if i.gender == gender:
                        print(f'姓名：{i.name}   \t性别：{i.gender}   \t年龄：{i.age}   \t电话：{i.tel}')
                        j.append(i)
                        continue
                if len(j) == 0:
                    print('查无此人')

            elif inp == '3':
                print('输入要查询人员的年龄段：')
                age_a = int(input('最小年龄：'))
                age_b = int(input('最大年龄：'))
                print(f'满足 {age_a} 到 {age_b} 岁的人员信息如下')
                j = []
                for i in self.person_list:
                    if i.age >= age_a and i.age <= age_b:
                        print(f'姓名：{i.name}   \t性别：{i.gender}   \t年龄：{i.age}   \t电话：{i.tel}')
                        j.append(i)
                        continue
                if len(j) == 0:
                    print('查无此人')

            elif inp == '4':
                tel = int(input('输入要查询人员的电话：'))
                print('人员信息如下')
                j = []
                for i in self.person_list:
                    if i.tel == tel:
                        print(f'姓名：{i.name}   \t性别：{i.gender}   \t年龄：{i.age}   \t电话：{i.tel}')
                        j.append(i)
                        continue
                if len(j) == 0:
                    print('查无此人')

            elif inp == '0':
                break
            else:
                print('输入有误，请从新输入。')

    # 显示所有人员信息
    def show_all_person(self):
        print('【 显示所有人员信息 】')
        print('姓名\t\t性别\t\t年龄\t\t电话')
        i = 0
        while i < len(self.person_list):
            # print(self.person_list[i]) # 原写法
            print(f'{self.person_list[i].name}\t\t{self.person_list[i].gender}\t\t{self.person_list[i].age}\t\t{self.person_list[i].tel}') #教程写法
            i += 1
        # print(self.person_list[0])

    # 保存人员信息
    def save_person(self):
        print('【 保存人员信息 】')
        # 打开文件
        name_f = input('输入保存的文件名：')
        f = open(f'{name_f}.data','w')

        # 文件写入数据
        # 涉及列表推导式和dict
        new_list = [i.__dict__ for i in self.person_list]
        f.write(str(new_list))

        f.close()
        print(f'文件保存成功：{name_f}.data')


    # 加载人员信息
    def load_person(self):
        print('【 打开已有人员信息文件 】')
        path_0 = input('输入文件加载路径（默认本目录）：')

        # 网上查到两种获取当前路径的方法
        # currentPath = os.path.dirname(os.path.abspath(__file__))
        currentPath = os.getcwd().replace('\\', '/')

        if len(path_0) == 0:
            path_0 = currentPath
        # 切换到相应目录
        os.chdir(path_0)
        path_2 = os.listdir()
        print(f'目录 {path_0} 文件列表如下：')
        for i in path_2:
            print(i)

        name_f = input('输入要打开的文件的全名（例：xxx.xx）：')
        # 打开文件
        try:
            f = open(f'{name_f}','r')
        except:
            # yn = input('未找到此文件，是否新建？（y/n）')
            # if yn == 'y':
            #     f = open(f'{name_f}','w')
            yn = input('未找到此文件，是否新建？（y/n）')
            if yn == 'y':
                f = open(f'{name_f}','w')
                # 读取数据
                data = f.read()
                # eval()将字符串中的数据转换成它原本的数据类型。（计算字符串中的有效的表达式，并返回一个对象）
                new_list = eval(data)
                # 涉及列表推导式
                self.person_list = [Person(i['name'], i['gender'], i['age'], i['tel']) for i in new_list]
                f.close()
            elif yn == 'n':
                self.run()
            # try:
            #     yn == 'n'
            # except:
            #     f.close()
            #     self.run()
            # else:
            #     f = open(f'{name_f}', 'w')
        # finally:


        self.show_all_person()


if __name__ == '__main__':
    ms = Management_system()
    ms.run()




