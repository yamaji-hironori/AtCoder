n, k = map(int, input().split())
MOD = 10**9 + 7
ans = 0
 
x = [0 for _ in range(k+1)]
 
for i in range(k, 0, -1):
    x[i] = pow(k//i, n, MOD)
    for j in range(2*i, k+1, i):
        x[i] -= x[j]
        x[i] %= MOD
    ans += i * x[i] % MOD
    ans %= MOD
print(ans)