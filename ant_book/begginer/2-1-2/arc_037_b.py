from collections import deque

Vertex, Side = map(int, input().split())
VerticesList = [[int(_)-1 for _ in input().split()] for i in range(Side)]
trees = [[] for _ in range(Vertex)]

for i_vertex, j_vertex in VerticesList:
    trees[i_vertex].append(j_vertex)
    trees[j_vertex].append(i_vertex)

# Check the number of times a vertex has been accessed.
# If there is a vertex that is accessed twice, it is a closed circuit.
check_closing = [0]*Vertex
inspection_vertex = deque()

num_trees = 0
for i_tree in range(Vertex):
    if check_closing[i_tree] != 0:
        continue

    pre_tree = -1
    is_closing = False
    is_inspected = [False]*Vertex
    is_inspected[i_tree] = True

    inspection_vertex.append([i_tree, pre_tree])
    while len(inspection_vertex) > 0:
        now_tree, pre_tree = inspection_vertex.pop()
        
        for next_tree in trees[now_tree]:
            if next_tree == pre_tree:
                continue

            check_closing[next_tree] += 1
            if check_closing[next_tree] >= 2:
                is_closing = True

            if not is_inspected[next_tree]:
                is_inspected[next_tree] = True
                inspection_vertex.append([next_tree, now_tree])

    if not is_closing:
        num_trees += 1

print(num_trees)