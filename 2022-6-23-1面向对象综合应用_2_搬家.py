"""
    P286【第14天】（加QQ：2250307122领取配套源码资料）
    综合应用_搬家

"""
class room():

    def __init__(self,area,fu):
        self.area = area
        self.state = ''
        self.free_area = self.area - fu.total_area

    def __str__(self):
        return f'房子剩余面积{self.free_area}，{self.state}'

    def add(self,fu):
        if self.free_area < fu.total_area:
            self.state = '装不下了'
        else:
            self.state = '还能装'


class furn():
    def __init__(self,name,area,amount,tatal_area):
        self.name = name
        self.area = area
        self.amount = amount
        self.total_area = tatal_area

    def __str__(self):
        return f'搬入{self.name}，单个占地面积：{self.area}，数量：{self.amount}，总占地面积：{self.total_area}'


name = input('输入要搬入的家具：')
area = int(input('占地面积：'))
amount = int(input('输入要搬入的数量：'))
fu = furn(name,area,amount,area * amount)
print(fu)

ro = room(500,fu)
ro.add(fu)
print(ro)







