"""
    P205【第11天】（加QQ：2250307122领取配套源码资料）
    学员管理系统

    需求：
    进入系统显示系统功能界面，功能如下：
    1、添加学员
    2、删除学员
    3、修改学员信息
    4、查询学员信息
    5、显示所有学员信息
    6、退出系统

"""

info = []

def info_print():
    print('=' * 30 + '学员管理系统')
    print('1、添加学员')
    print('2、删除学员')
    print('3、修改学员信息')
    print('4、查询学员信息')
    print('5、显示所有学员信息')
    print('6、退出系统')
    print('=' * 30)
    x = input('输入数字选择对应功能：')

    # 用while True循环实现功能的从复加载，直到确认退出
    while True:
        if int(x) == 1:
            add_stu()
            break
        elif int(x) == 2:
            del_stu()
            break
        elif int(x) == 3:
            edi_stu()
            break
        elif int(x) == 4:
            inq_stu()
            break
        elif int(x) == 5:
            info_all()
            break
        elif int(x) == 6:
            yn = input('确认要退出吗？（y/n）')
            if yn == 'y':
                return
            else:
                break
        else:
            print('输入有误，请从新输入:')
            break

    info_print()

def add_stu():
    global info

    new_name = input('输入姓名：')
    new_sex = input('输入性别：')
    new_id = int(input('输入学号：'))
    new_num = int(input('输入电话：'))

    for i in info:
        if new_name == i['name'] and new_id == i['id']:
            print('用户已存在')
            return

    info_dict = {}
    info_dict['name'] = new_name
    info_dict['sex'] = new_sex
    info_dict['id'] = new_id
    info_dict['num'] = new_num

    info.append(info_dict)
    for i in info:
        print(i)


def del_stu():
    global info
    for i in info:
        print(i)
    name = input('输入要删除的用户姓名：')

    for i in info:
        if name == i['name']:
            print(f'要删除的用户信息：{i}')
            yn = input('是否删除？（y/n）')
            if yn == 'y':
                info.remove(i)
                print('删除成功！')
                print('删除后用户信息列表：')
                for i in info:
                    print(i)
                break # 跳出for循环
    else: # for正常遍历完之后执行的代码
        print('用户不存在')



def edi_stu():
    global info
    for i in info:
        print(i)
    name = input('输入要修改的用户名：')

    for i in info:
        if name == i['name']:
            print(f'要修改的用户信息：{i}')
            key = input('输入要修改的项目：')
            if key == 'name':
                edi_name = input('输入修改后的姓名：')
                i['name'] = edi_name
                print('修改成功！')
                print('修改后用户信息列表：')
                for i in info:
                    print(i)
                return
            elif key == 'sex':
                edi_sex = input('输入修改后的性别：')
                i['sex'] = edi_sex
                print('修改成功！')
                print('修改后用户信息列表：')
                for i in info:
                    print(i)
                return
            elif key == 'id':
                edi_id = input('输入修改后的ID：')
                i['id'] = edi_id
                print('修改成功！')
                print('修改后用户信息列表：')
                for i in info:
                    print(i)
                return
            else:
                edi_num = input('输入修改后的电话：')
                i['num'] = edi_num
                print('修改成功！')
                print('修改后用户信息列表：')
                for i in info:
                    print(i)
                return
    else: # for正常遍历完之后执行的代码
        print('用户不存在')

def inq_stu():
    global info
    for i in info:
        print(i)
    print('1、按名字查询')
    print('2、按学号查询')
    put = int(input('请选择按名字还是学号查找：'))
    if put == 1:
        info_any = input('请输入姓名：')
        for i in info:
            if info_any in i['name']:
                print(f'姓名为 {info_any} 的用户信息如下：')
                print(i)
                return
    elif put == 2:
        info_any = input('请输入学号：')
        for i in info:
            if info_any == i['id']:
                print(f'学号为 {info_any} 的用户信息如下：')
                print(i)
                return
    else:  # for正常遍历完之后执行的代码
        print('用户不存在')

def info_all():
    print('所有用户信息如下：')
    print('===姓名===\t===性别===\t===学号===\t===电话===')
    for i in info:
        print(f"   {i['name']}   \t   {i['sex']}   \t   {i['id']}   \t   {i['num']}   ")

# def exit():
#     yn = input('确认退出系统？（y/n）')
#     if yn == 'y':
#         return False
#     else:
#         return True


info_print()









