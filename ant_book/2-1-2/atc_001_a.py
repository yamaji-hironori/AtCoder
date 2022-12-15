from collections import deque

road_que = deque()

Height, Width = map(int, input().split())
Sections = [input() for _ in range(Height)]
status_sections = [[0] * Width for _ in range(Height)]

for y, row in enumerate(Sections):
    if 's' in row:
        start_y = y
        start_x = row.index('s')

road_que.append([start_y, start_x])
while len(road_que) > 0:
    y, x = road_que.pop()
    status_sections[y][x] = 1

    for dy, dx in [(-1,0), (0,-1), (1,0), (0,1)]:
        next_y, next_x = (y + dy), (x + dx)
        if (next_y <= -1 or Height <= next_y) or \
                                              (next_x <= -1 or Width <= next_x):
            continue
        
        if Sections[next_y][next_x] == 'g':
            print('Yes')
            exit()

        if status_sections[next_y][next_x] == 0 and \
                                                Sections[next_y][next_x] == '.':
            road_que.append([next_y, next_x])

print('No')