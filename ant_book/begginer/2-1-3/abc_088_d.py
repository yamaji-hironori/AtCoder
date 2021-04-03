from collections import deque

Height, Width = map(int, input().split())
Map = [input() for _ in range(Height)]

y_start, x_start = 0, 0
y_goal, x_goal = Height-1, Width-1

min_step_map = [[-1]*Width for _ in range(Height)]
min_step_map[y_start][x_start] = 0
reserch_point = deque()
reserch_point.append([y_start, x_start])
while len(reserch_point) > 0:
    y_now, x_now = reserch_point.popleft()

    for dy, dx in [(-1,0), (0,-1), (1,0), (0,1)]:
        y_next, x_next = y_now+dy, x_now+dx
        if (y_next <= -1 or Height <= y_next) or \
                                              (x_next <= -1 or Width <= x_next):
            continue

        if y_next == y_goal and x_next == x_goal:
            min_step_map[y_goal][x_goal] = min_step_map[y_now][x_now] + 1
            break

        if Map[y_next][x_next] == '.' and min_step_map[y_next][x_next] == -1:
            min_step_map[y_next][x_next] = min_step_map[y_now][x_now] + 1
            reserch_point.append([y_next, x_next])
        
    else:
        continue
    break

else:
    print(-1)
    exit()

min_step = min_step_map[y_goal][x_goal]
count_black = 0
for y in range(Height):
    for x in range(Width):
        if Map[y][x] == '#':
            count_black += 1

# Since the starting point is not included in 'min_step',
# it is excluded from the total number of maps.
total_point = Height * Width - 1

score = total_point - count_black - min_step
print(score)