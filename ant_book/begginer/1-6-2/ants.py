n, l, t = map(int, input().split())

xw = []
for _ in range(n):
    x, w = map(int, input().split())
    xw.append([x, w])

print(xw)
ant_list = []
for x, w in xw:
    if w == 1:
        x += t
    else:
        x -= t
        
    ant_list.append(x)

ant_list.sort()
print(ant_list)

for i_ant in ant_list:
    print((i_ant % l))