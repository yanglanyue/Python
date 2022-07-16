"""
    P286【第14天】（加QQ：2250307122领取配套源码资料）
    综合应用_搬家（）教程写法

"""
class room():

    def __init__(self,address,area,furn):
        # 地理位置
        self.address = address
        # 房子面子
        self.area = area
        # 剩余面积
        self.free_area = self.area - furn.total_area
        # 搬入家具的总面积
        self.furns_area = furn.total_area
        # 家具列表
        self.furns = []

    def __str__(self):
        return f'房子位置：{self.address}，搬入的家具占地面积：{self.furns_area}，剩余面积{self.free_area}，家具有：{self.furns}'

    def add_furn(self,furn):
        if self.area >= furn.total_area:
            self.furns.append(furn.name * furn.amount)
            self.area -= furn.area
        else:
            print('家具太大，剩余面积不够，无法搬入！')


class  furn():
    def __init__(self,name,area,amount):
        self.name = name
        self.area = area
        self.amount = amount
        self.total_area = self.area * self.amount

    def __str__(self):
        return f'搬入{self.name}，每件占地面积：{self.area}，数量：{self.amount}，总占地面积：{self.total_area}'


name = input('输入要搬入的家具：')
area = int(input('占地面积：'))
amount = int(input('输入要搬入的数量：'))
fu = furn(name,area,amount)
print(fu)

ro = room('纽约',100,fu)

ro.add_furn(fu)
print(ro)





