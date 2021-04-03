import sys

def main():
    D, N = map(int, input().split())
    T = [int(input()) for i in range(D)]
    ABC = [[int(_) for _ in input().split()] for i in range(N)]

    dp = [[None for _ in range(N)] for _ in range(D)]
    for i, i_abc in enumerate(ABC):
        if i_abc[0] <= T[0] and T[0] <= i_abc[1]:
            dp[0][i] = 0

    for i_D in range(1, D):
        for i_N in range(N):
            if dp[i_D-1][i_N] is None:
                continue
            
            for j_N, j_abc in enumerate(ABC):
                if j_abc[0] <= T[i_D] and T[i_D] <= j_abc[1]:
                    if dp[i_D][j_N] is None:
                        dp[i_D][j_N] = 0
                    dp[i_D][j_N] = max(dp[i_D][j_N], \
                                abs(ABC[j_N][2] - ABC[i_N][2]) + dp[i_D-1][i_N])

    for i in range(N):
        if dp[D-1][i] is None:
            dp[D-1][i] = 0

    ans = max(dp[D-1])
    print(ans)

    return


if __name__ == "__main__":
    main()
    sys.exit(0)