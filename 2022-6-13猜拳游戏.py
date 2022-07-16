"""
猜拳游戏
"""

# 导入random随机数生成器
import random

x = int(input('1 -- 剪刀，2 -- 石头，3 -- 布，请出拳：'))

computer = random.randint(1,3)

if computer == 1:
    com = '剪刀'
elif computer == 2:
    com = '石头'
else:
    com = '布'

if x == computer:
    print('平手')
else:
    if (x == 1) and (computer == 2):
        print(f'电脑出拳：{com}，电脑获胜')
    elif (x == 1) and (computer == 3):
        print(f'电脑出拳：{com}，玩家获胜')
    elif (x == 2) and (computer == 1):
        print(f'电脑出拳：{com}，玩家获胜')
    elif (x == 2) and (computer == 3):
        print(f'电脑出拳：{com}，电脑获胜')
    elif (x == 3) and (computer == 1):
        print(f'电脑出拳：{com}，电脑获胜')
    elif (x == 3) and (computer == 2):
        print(f'电脑出拳：{com}，玩家获胜')


"""
三目运算符
"""

a = 1
b = 2

c = a if a > b else b
print(c)

aa = int(input('请输入一个数字：'))
bb = random.randint(0,100000000)
cc = aa - bb if aa >= bb else bb - aa
print(f'随机数为：{bb}，{bb} - {aa} = {cc}') if aa < bb else print(f'随机数为：{bb}，{aa} - {bb} = {cc}')