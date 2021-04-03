from collections import deque

IslandsMap = [input() for _ in range(10)]

# Numbering the island and the sea around it.
# If the number of islands and the number attached to the sea are equivalent,
# it is possible to make one island.
status_landfill = [[0]*10 for _ in range(10)]
inspected_area = [[0]*10 for _ in range(10)]

inspection_point = deque()
num_island = 0
max_adjacent = 0

def check_extent_island():
    global max_adjacent
    global num_island
    num_island += 1
    
    while len(inspection_point) > 0:
        y_now, x_now = inspection_point.pop()
        status_landfill[y_now][x_now] = num_island

        for dy, dx in [(-1,0), (0,-1),(1,0),(0,1)]:
            y_next, x_next = y_now+dy, x_now+dx
            if (y_next<=-1 or 10<=y_next) or (x_next<=-1 or 10<=x_next):
                continue

            #　Calculate the number of times adjacent to the island.
            if IslandsMap[y_next][x_next] == 'x' and \
                                            inspected_area[y_next][x_next] == 0:
                status_landfill[y_next][x_next] += 1
                inspected_area[y_next][x_next] = 1
                max_adjacent = max(max_adjacent,status_landfill[y_next][x_next])

            elif IslandsMap[y_next][x_next] == 'o' and \
                                           status_landfill[y_next][x_next] == 0:
                inspection_point.append([y_next, x_next])
    return 

for y_map in range(10):
    for x_map in range(10):
        if IslandsMap[y_map][x_map]=='o' and status_landfill[y_map][x_map]==0:
            inspection_point.append([y_map, x_map])
            
            check_extent_island()
            inspected_area = [[0]*10 for _ in range(10)]

if num_island == max_adjacent:
    print('YES')
else:
    print('NO')