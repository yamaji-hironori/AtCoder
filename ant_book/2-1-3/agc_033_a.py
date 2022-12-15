from collections import deque

Height, Width = map(int, input().split())
Map = [input() for _ in range(Height)]
min_step_map = [[10**6]*Width for _ in range(Height)]
research_point = deque()

# Find the minimum number of steps from all blacks.
# The maximum number of the obtained minimum steps is the answer.
def search_min_step():
    while len(research_point) > 0:
        y_now, x_now = research_point.popleft()
        
        for dy, dx in [(-1,0), (0,-1), (1,0), (0,1)]:
            y_next, x_next = y_now+dy, x_now+dx
            if (y_next <= -1 or Height <= y_next) or \
                                              (x_next <= -1 or Width <= x_next):
                continue
            
            if Map[y_next][x_next] == '#' or \
                 min_step_map[y_next][x_next] <= min_step_map[y_now][x_now] + 1:
                continue
            else:
                min_step_map[y_next][x_next] = min_step_map[y_now][x_now] + 1
                research_point.append([y_next, x_next])

for y in range(Height):
    for x in range(Width):
        if Map[y][x] == '#':
            min_step_map[y][x] = 0
            research_point.append([y, x])

search_min_step()

max_step = 0
for y in range(Height):
    max_step = max(max_step, max(min_step_map[y]))

print(max_step)