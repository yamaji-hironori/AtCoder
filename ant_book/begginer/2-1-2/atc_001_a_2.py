from collections import deque

Height, Width = map(int, input().split())
Sections = [input() for _ in range(Height)]
is_road_passed = [[False]*Width for _ in range(Height)]

for y in range(Height):
    for x in range(Width):
        if Sections[y][x] == 's':
            y_start = y
            x_start = x
            break
    else:
        continue
    break

road_to_pass = deque()
road_to_pass.append([y_start, x_start])
while len(road_to_pass) > 0 :
    y_now, x_now = road_to_pass.pop()
    is_road_passed[y_now][x_now] = True

    for dy, dx in [(-1,0), (0,-1), (1,0), (0,1)]:
        y_next, x_next = y_now+dy, x_now+dx

        if (y_next<=-1 or Height<=y_next) or (x_next<=-1 or Width<=x_next):
            continue

        if Sections[y_next][x_next] == 'g':
            print('Yes')
            exit()

        if Sections[y_next][x_next]=='.' and not is_road_passed[y_next][x_next]:
            road_to_pass.append([y_next, x_next])

print('No')
exit()