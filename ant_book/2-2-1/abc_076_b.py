N = int(input())
K = int(input())

ans = 1
for _ in range(N):
    double = ans * 2
    add = ans + K
    ans = min(double, add)

print(ans)