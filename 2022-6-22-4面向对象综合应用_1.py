"""
    P279【第14天】（加QQ：2250307122领取配套源码资料）
    综合应用

"""
# 烤地瓜
class SP():

    def __init__(self):
        self.cook_time = 0
        self.cook_static = '生的'
        self.condiments = []

    def __str__(self):
        return f"这个地瓜烤了{self.cook_time}分钟，{self.cook_static}，加了调料：{self.condiments}"

    def cook(self,time):
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_static = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_static = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_static = '熟了'
        else:
            self.cook_static = '烤糊了'

    def add_condiments(self,condiments):
        self.condiments.append(condiments)


sp_1 = SP()
print(sp_1)
sp_1.cook(2)
print(sp_1)
sp_1.cook(2)
print(sp_1)
sp_1.cook(2)
sp_1.add_condiments('辣椒')
sp_1.add_condiments('盐')
print(sp_1)








