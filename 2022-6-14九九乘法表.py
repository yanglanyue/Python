"""
九九乘法表
"""

y = 1
while y <= 9:
    x = 1
    while x <= y:
        print(f'{x} x {y} = {x * y}', end='\t')
        x += 1
    y += 1
    print()

# 网络for循环版本
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()





