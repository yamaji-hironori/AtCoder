import sys
import math

def main():
    N, K = map(int, input().split())
    A = [int(input()) for i in range(N)]

    cumul_sum = [0]*(N+1)
    for i, i_A in enumerate(A, 1):
        cumul_sum[i] = cumul_sum[i-1] + i_A

    dp = [[0]*(N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, i+1):
            if dp[i-1][j-1] == 0:
                min_win = 1
            else:
                min_win = math.ceil(dp[i-1][j-1]*A[i-1]/cumul_sum[i-1])

            if min_win <= A[i-1]:
                dp[i][j] = dp[i-1][j-1] + min_win
            else:
                dp[i][j] = dp[i-1][j-1]

    for j in range(N, -1, -1):
        if dp[-1][j] <= K:
            break
    
    print(j)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)