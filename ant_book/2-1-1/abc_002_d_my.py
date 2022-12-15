N, M = map(int, input().split())
XY = [[int(x)-1 for x in input().split()] for i in range(M)]

# If there is no human relationship, you can only create a group of one person.
max_group = 1

# The assumed group is represented by a binary number.
for assumed_group in range(1, 2**N):
    now_group =  set()

    for i_legislator in range(0, N):
        if assumed_group & (1 << i_legislator):
            for mem in now_group:
                if not [mem, i_legislator] in XY:
                    break
            else:
                now_group.add(i_legislator)

    max_group = max(max_group, len(now_group))

print(max_group)