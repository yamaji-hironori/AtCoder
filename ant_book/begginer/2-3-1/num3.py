import sys

def main():
    D = int(input())
    N = list(reversed(input()))
    mod = 1000000007

    dp = [[0 for _ in range(D)] for _ in range(len(N))]
    dp_max = [[0 for _ in range(D)] for _ in range(len(N))]

    for i in range(int(N[0])):
        dp[0][i % D] += 1

    for i in range(10):
        dp_max[0][i % D] += 1

    for i_N in range(1, len(N)):
        # case of 'j' < N[i_N]
        for j in range(int(N[i_N])):
            for k in range(D):
                dp[i_N][(k+j)%D] += dp_max[i_N-1][k]
                dp[i_N][(k+j)%D] = dp[i_N][(k+j)%D] % mod

        # case of 'j' = N[i_N]
        for k in range(D):
            dp[i_N][(k+int(N[i_N]))%D] += dp[i_N-1][k]
            dp[i_N][(k+int(N[i_N]))%D] = dp[i_N][(k+int(N[i_N]))%D] % mod

        # for case of 'j' < N[i_N+1]
        for j in range(10):
            for k in range(D):
                dp_max[i_N][(k+j)%D] += dp_max[i_N-1][k]
                dp_max[i_N][(k+j)%D] = dp_max[i_N][(k+j)%D] % mod

    print(dp[-1][0] - 1)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)