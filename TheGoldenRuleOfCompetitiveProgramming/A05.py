
def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            k = K - i - j
            if 1 <= k and k <= N: ans += 1
    
    print(ans)


main()
