N, K = list(map(int, input().split()))

n = N % K
n_another = K - n

ans = min(n, n_another)
print(ans)