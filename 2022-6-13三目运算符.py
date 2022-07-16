"""
三目运算符
"""
import random

a = 1
b = 2

c = a if a > b else b
print(c)

aa = int(input('请输入一个数字：'))
bb = random.randint(0,100000000)
cc = aa - bb if aa >= bb else bb - aa
print(f'随机数为：{bb}，{bb} - {aa} = {cc}') if aa < bb else print(f'随机数为：{bb}，{aa} - {bb} = {cc}')



