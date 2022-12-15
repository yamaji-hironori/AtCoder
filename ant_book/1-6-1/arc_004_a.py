import math

n = int(input())

xy = []
for _ in range(n):
    x, y = map(int, input().split())
    xy.append([x, y])

enum_list = []
for i_n in range(n):
    for j_n in range(i_n+1, n):
        enum_list.append([i_n, j_n])

max_ans = 0
for i_e in enum_list:
    x_square = (xy[int(i_e[0])-1][0] - xy[int(i_e[1])-1][0])**2
    y_square = (xy[int(i_e[0])-1][1] - xy[int(i_e[1])-1][1])**2

    if (x_square + y_square) > max_ans:
        max_ans = x_square + y_square

ans = math.sqrt(max_ans)
print(ans)