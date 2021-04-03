N, A, B = map(int, input().split())

mod = N % (A+B)
ans = 0
if 0 < mod and mod <= A:
    ans = mod
elif mod != 0:
    ans = A

ans += (N // (A+B)) * A
print(ans)