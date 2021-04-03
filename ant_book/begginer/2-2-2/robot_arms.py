NumRobot = int(input())
RobotList = [[int(_) for _ in input().split()] for i in range(NumRobot)]

edge_list = []
for i_coordinate, i_arm in RobotList:
    edge_list.append([i_coordinate - i_arm, i_coordinate + i_arm])

edge_list = sorted(edge_list, key=lambda x: x[1])

total_robot = 1
right_edge_compare = edge_list[0][1]

for i_left_edge, i_right_edge in edge_list[1:]:
    if i_left_edge < right_edge_compare:
        continue

    right_edge_compare = i_right_edge
    total_robot += 1

print(total_robot)