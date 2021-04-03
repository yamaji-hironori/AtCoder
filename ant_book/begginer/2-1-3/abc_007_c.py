from collections import deque

Line, Row = map(int, input().split())
Ystart, Xstart = map(int, input().split())
Ygoal, Xgoal = map(int, input().split())
Sections = [input() for _ in range(Line)]
min_step = [[2510]*Row for _ in range(Line)]

min_step[Ystart-1][Xstart-1] = 0
confirm_road = deque()
confirm_road.append([Ystart-1, Xstart-1])

while len(confirm_road) > 0:
    y_now, x_now = confirm_road.pop()
    next_step = min_step[y_now][x_now] + 1

    for dy, dx in [(-1,0), (0,-1), (1,0), (0,1)]:
        y_next, x_next = y_now+dy, x_now+dx
        if (y_next <= -1 or Line <= y_next) or (x_next <= -1 or Row <= x_next):
            continue

        if Sections[y_next][x_next] == '#' or \
                                          next_step >= min_step[y_next][x_next]:
            continue

        min_step[y_next][x_next] = next_step
        confirm_road.append([y_next, x_next])

print(min_step[Ygoal-1][Xgoal-1])