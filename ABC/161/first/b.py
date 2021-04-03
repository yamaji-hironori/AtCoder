N, M, *A = map(int, open(0).read().split())

total = sum(A)
can_select_num = 0

for a in A:
    if a >= total/(4*M):
        can_select_num += 1

if can_select_num >= M:
    print('Yes')
else:
    print('No')