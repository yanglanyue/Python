"""
    P354【第19天】（加QQ：2250307122领取配套源码资料）
    创建 Person 类

"""
class Person(object):
    def __init__(self,name,gender,age,tel):
        self.name = name
        self.gender = gender
        self.age = age
        self.tel = tel

    def __str__(self):
        return f'姓名：{self.name}\t\t性别：{self.gender}\t\t年龄：{self.age}\t\t电话：{self.tel}'





if __name__ == '__main__':
    p_00 = Person('Tom','男',25,13033333333)
    print(p_00)







