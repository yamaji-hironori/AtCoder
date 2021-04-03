NumIslands, NumRequest = map(int, input().split())
ListConflict = [[int(_) for _ in input().split()] for i in range(NumRequest)]

ListConflict = sorted(ListConflict, key=lambda x: x[1])
right_island_compare = ListConflict[0][1]
total_remove = 1

for i_left_island, i_right_island in ListConflict[1:]:
    if i_left_island < right_island_compare:
        continue

    right_island_compare = i_right_island
    total_remove += 1

print(total_remove)