import sys

def main():
    D = int(input())
    N = list(reversed(input()))
    mod = 1000000007

    dp = [[0 for _ in range(D)] for _ in range(len(N))]
    dp_max = [[0 for _ in range(D)] for _ in range(len(N))]

    for i in range(0, int(N[0])+1):
        dp[0][i % D] += 1
    
    for i in range(0, 10):
        dp_max[0][i % D] += 1

    for i_N in range(1, len(N)):
        # case of 'j' < N[i_N]
        for j in range(0, int(N[i_N])):
            for k in range(D):
                dp[i_N][(j+k)%D] += dp_max[i_N-1][k]
                dp[i_N][(j+k)%D] = dp[i_N][(j+k)%D] % mod

        # case of 'j' = N[i_N]
        for k in range(D):
            dp[i_N][(k+int(N[i_N]))%D] += dp[i_N-1][k]
            dp[i_N][(k+int(N[i_N]))%D] = dp[i_N][(k+int(N[i_N]))%D] % mod

        # case of 'j+1' < N[i_N]
        for j in range(0, 10):
            for k in range(D):
                dp_max[i_N][(j+k)%D] += dp_max[i_N-1][k]
                dp_max[i_N][(j+k)%D] = dp_max[i_N][(j+k)%D] % mod

    print(dp[-1][0]-1)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)