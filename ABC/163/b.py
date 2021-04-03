N, M = map(int, input().split())
A = list(map(int, input().split()))

sum_a = sum(A)
if N < sum_a:
    print(-1)
else:
    print(N - sum_a)