"""
条件语句
"""

x = input('输入年龄：')
X = int(x)
set = 5;

# 条件成立执行下面缩进的代码，未缩进的代码不属于if条件代码块
if 120 >= X >= 18:
    print(f'{X}岁是成年人')
    if set > 0:
        print('请坐')
    else:
        print('没位置了，请稍等')
elif X > 120:
    print(f'{X}岁？，别开玩笑！请准确输入年龄。')
else:
    print(f'{X}岁还未成年\n请离开')

print('欢迎光临')






