import random
from pyamaze import maze
print("Nhap so dinh:")
n_dinh = int(input())
arr = [[0] * n_dinh for i in range(n_dinh)]
# print(arr)
# arr_random = [0,0,0,0,0,0,0,0,1,1]
# for i in range(n_dinh):
#     for j in range(n_dinh):
#         if i != j:
#             rd_num = random.randint(0,9)
#             rd = arr_random[rd_num]
#             arr[i][j] = rd
# for 
m = maze(15,20)
m.CreateMaze(x=1,y=1)
m.run()