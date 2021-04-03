Bingo_list = [[int(_) for _ in input().split()] for i in range(3)]

cross_line = []
reverse_cross = []
for i in range(3):
    vertiual_line = []
    cross_line.append(Bingo_list[i][i])
    reverse_cross.append(Bingo_list[i][2-i])
    for j_line in Bingo_list[:3]:
        vertiual_line.append(j_line[i])
    Bingo_list.append(vertiual_line)

Bingo_list.append(cross_line)
Bingo_list.append(reverse_cross)

N = int(input())
SelectNum = [int(input()) for _ in range(N)]

for i_line in Bingo_list:
    for i_num in i_line:
        if not i_num in SelectNum:
            break
    else:
        ans = 'Yes'
        break
else:
    ans = 'No'

print(ans)