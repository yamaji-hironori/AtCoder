import sys

def main():
    d = int(input())
    n = list(reversed(input().rstrip()))
    
    mod = 10**9+7
    dp1 = [[0] * d for _ in range(len(n))]
    dp2 = [[0] * d for _ in range(len(n))]
    
    for i in range(int(n[0]) + 1):
        dp1[0][i%d] += 1
    
    for i in range(10):
        dp2[0][i%d] += 1
    
    # i is digit
    for i in range(1, len(n)):
        # j is 上限
        for j in range(int(n[i])):
            # k is mod
            for k in range(d):
                dp1[i][k] += dp2[i-1][(k-j) % d]
                dp1[i][k] %= mod
    
        # k is mod
        for k in range(d):
            dp1[i][k] += dp1[i-1][(k-int(n[i])) % d]
            dp1[i][k] %= mod
    
        # j is 上限
        for j in range(10):
            for k in range(d):
                dp2[i][k] += dp2[i-1][(k-j) % d]
                dp2[i][k] %= mod
    
    return


if __name__ == "__main__":
    main()
    sys.exit(0)