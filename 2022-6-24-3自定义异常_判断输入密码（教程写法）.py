"""
    P329【第17天】（加QQ：2250307122领取配套源码资料）
    自定义异常

"""
# ====================================================================================================================== 教程写法
print('=============================================教程写法')
class ShortInputError(Exception):
    def __init__(self,length,min_len):
        self.length =length
        self.min_len = min_len

    def __str__(self):
        return f'设置的密码至少要 {self.min_len} 位以上，您设置的只有 {self.length} 位，请从新设置。'

def main():
    try:
        con = input('请设置密码：')
        if len(con) < 3:
            raise ShortInputError(len(con),3)
    except Exception as result:
        print(result)
    else:
        print('密码设置成功！')

main()

# ====================================================================================================================== 自编写法
# 用户输入注册密码，密码至少设定位数以上
print('=============================================自编写法')
class InputCheck(Exception):

    def __init__(self,len):
        self.len = len
        self.con = ''

    def __str__(self):
        return f'设置的密码至少要 {self.len} 位以上，您设置的只有 {len(self.con)} 位，请从新设置。'

    def input_check(self):
        print(f'注意设置的密码长度至少 {self.len} 位。')
        while True:
            try:
                self.con = input('请设置密码：')
                if len(self.con) < self.len:
                    raise InputCheck()
            except:
                print(self)
            else:
                print('密码设置成功！')
                break


inp1 = InputCheck(15)
inp1.input_check()




