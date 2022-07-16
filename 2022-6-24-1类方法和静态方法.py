"""
    P313【第14天】（加QQ：2250307122领取配套源码资料）
    类方法和静态方法

    类方法的特点
    需要使用装饰器 @classmethod 来标识其为类方法，对于类方法，第一个参数必须是类对象，一般以 cls 作为第一个参数

    静态方法的特点
    需要使用装饰器 @staticmethod 来标识其为静态方法，既不需要传递类对象也不需要传递实例对象，形参没有 (self) 或 (cls)
    静态方法可以通过 实例对象 和 类对象 去访问

"""
class miner():
    def mining(self):
        print('开始挖矿！')

class miner_BTC(miner):
    normal = 110
    __overclock = 130

    def mining(self):
        print(f'开始挖BTC！算力：{self.normal} T')

    # ================================================================================================================== 创建类方法，一般以 cls 作为第一个参数
    @classmethod
    def overclock_mining(cls):
        print(f'开始超频挖BTC！算力：{cls.__overclock} T')

    # ================================================================================================================== 创建静态方法，无需任何形参
    @staticmethod
    def error_mining():
        print(f'挖BTC故障！算力：0 T')


class miner_ETH(miner):
    normal = 120
    __overclock = 129

    def mining(self):
        print(f'开始挖ETH！算力：{self.normal} M')

    # ================================================================================================================== 创建类方法，一般以 cls 作为第一个参数
    @classmethod
    def overclock_mining(cls):
        print(f'开始超频挖ETH！算力：{cls.__overclock} M')

    # ================================================================================================================== 创建静态方法，无需任何形参
    @staticmethod
    def error_mining():
        print(f'挖ETH故障！算力：0 M')

class person():
    def work(self,miner):
        miner.mining()

    def error_work(self,miner):
        miner.error_mining()


s19_Pro = miner_BTC()
s19_Pro.overclock_mining() # =========================================================================================== 对象调用类方法
miner_BTC.overclock_mining() # ========================================================================================= 类调用类方法
s19_Pro.error_mining() # =============================================================================================== 对象调用静态方法
miner_BTC.error_mining() # ============================================================================================= 类调用类方法

RTX3090 = miner_ETH()
RTX3090.overclock_mining() # =========================================================================================== 对象调用类方法

Tom = person()
Tom.work(s19_Pro)
Tom.work(RTX3090)
Tom.error_work(s19_Pro)
Tom.error_work(RTX3090)











