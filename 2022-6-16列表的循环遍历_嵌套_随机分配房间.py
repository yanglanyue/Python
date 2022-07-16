"""
    P125【第六天】随机分配办公室
    列表的循环遍历
"""

name_list = ['Tom','Lucy','Lily','Jack','Bob','Rose','Piter','Elon','Bill','Dell','Jobs','William','SUSHI','Uni','Cake','CURVE','BTC','ETH','DOT']

# while循环
i = 0
while i < len(name_list):
    print(name_list[i],end=' ')
    i += 1

print()
# for循环
for i in name_list:
    print(i,end=' ')

"""
    列表嵌套
"""
print()

list_X = [name_list,[0,1,2,3,4,5,6,7,8,9]]
print(list_X[0][2])

"""
    将列表中的人随机分配到N个房间
    将每个房间人员依次遍历
"""
import random

list_room = [[],[],[],[],[]]

i = -len(name_list)+1
j = 0

while i <= len(name_list):

    n = random.randint(0, len(name_list) - 1)
    r = random.randint(0, len(list_room) - 1)

    if i <= len(name_list):
        list_room[r].append(name_list[n])
        del name_list[n]
        i += 1

print(list_room)
k = 0
for x in list_room:
    print(f'{k+1}号房间人员如下：')
    for y in list_room[k]:
        print(y,end=' ')
    k += 1
    print()

