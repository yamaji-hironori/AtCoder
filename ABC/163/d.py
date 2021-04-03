def combination(n, x, mod=10**9+7):
    # nCx
    # 組み合わせ
    # ex) combination(5, 2) = 10
    factorial = [1] * (n+1)
    t = 1
    for i in range(1, n+1):
        t = (t * i) % mod
        factorial[i] = t
    tmp = factorial[n]
    tmp = (tmp * pow(factorial[x], mod-2, mod)) % mod
    tmp = (tmp * pow(factorial[n-x], mod-2, mod)) % mod
    return tmp

N, K = map(int, input().split())

ans = 0
for i_k in range(K, N+2):
    ans += combination(N+1, i_k)

print(ans)