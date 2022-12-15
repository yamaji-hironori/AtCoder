from collections import deque

Height, Width, FactoryNum = map(int, input().split())
Map = [input() for _ in range(Height)]

for y in range(Height):
    for x in range(Width):
        if Map[y][x] == 'S':
            y_start = y
            x_start = x
            break
    else:
        continue
    break

def search_min_step(y_start, x_start, goal_factory_num):
    search_point = deque()
    search_point.append([y_start, x_start])
    min_step_map = [[-1]*Width for _ in range(Height)]
    min_step_map[y_start][x_start] = 0

    while len(search_point) > 0:
        y_now, x_now = search_point.popleft()

        for dy, dx in [(-1,0), (0,-1), (1,0), (0,1)]:
            y_next, x_next = y_now+dy, x_now+dx
            if (y_next <= -1 or Height <= y_next) or \
                                              (x_next <= -1 or Width <= x_next):
                continue

            if Map[y_next][x_next]!='X' and min_step_map[y_next][x_next]==-1:
                min_step_map[y_next][x_next] = min_step_map[y_now][x_now] + 1
                search_point.append([y_next, x_next])

            if Map[y_next][x_next] == str(goal_factory_num):
                return min_step_map[y_now][x_now]+1, y_next, x_next

total_step = 0
for i_factory in range(1, FactoryNum+1):
    min_step, y_start, x_start = search_min_step(y_start, x_start, i_factory)
    
    total_step += min_step

print(total_step)