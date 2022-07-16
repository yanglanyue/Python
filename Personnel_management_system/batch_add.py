from management_system import *
from Person import *
import random

ms = Management_system()

class batch_add():
    def __init__(self):
        self.name = ''
        self.gender = ''
        self.age = 0
        self.names_g = ['Lucy','Lily','Rose','Ava','Belle','Anthea','Diana','Flora',
                      'Jenny','Lynn','Melissa','Olive','Rosa','Susan','Vivian','Shirley',
                        'Roberta','Nita','Martha','Sonia','Nan','Marian','Kim','Leila',
                        'Ivy','Helen','Ella','Doris','Anita']

        self.names_b = ['Tom','Jack','Bob','Piter','Elon','Bill','Dell','Jobs','William',
                       'Aaron','Absalom','Armin','Bard','Barry','Ben','Bernd','Bowen',
                       'Carl','Charles','Clark','Dan','David','Dick','Duke','Eden','Fido'
                       ,'Frank','Gordon','Henry','Jim','King']

    def creat_name(self):
        gb = random.randint(1,100)
        if 1 <= gb <= 59:
            x = random.randint(0, len(self.names_g) - 1)
            self.name = self.names_g[x]
            self.gender = '女'
            self.age = random.randint(1,80)
        elif gb == 60:
            x = random.randint(0, len(self.names_g) - 1)
            self.name = self.names_g[x]
            self.gender = '女'
            self.age = random.randint(70, 130)
        elif 61 <= gb <= 99:
            x = random.randint(0, len(self.names_b) - 1)
            self.name = self.names_b[x]
            self.gender = '男'
            self.age = random.randint(1, 80)
        elif gb == 100:
            x = random.randint(0, len(self.names_b) - 1)
            self.name = self.names_b[x]
            self.gender = '男'
            self.age = random.randint(70, 130)

    def add_pro(self):
        num = int(input('输入要添加的用户数量：'))
        i = 0

        while i <num:
            r = random.randint(999,9999999999)
            self.creat_name()
            p = Person(self.name, self.gender, self.age, 20000000000 - r)
            ms.person_list.append(p)
            i += 1

        ms.show_all_person()
        ms.run()






