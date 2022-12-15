import sys
import bisect

def main():
    N = int(input())
    C = [int(input()) for i in range(N)]
    INF = float('inf')

    dp = [INF]*(N+2)
    dp[0] = -INF

    for i_c in C:
        insert_index = bisect.bisect_left(dp, i_c)
        dp[insert_index] = i_c

    for i, i_dp in enumerate(dp):
        if i_dp == INF:
            ans = N - (i-1)
            break
    
    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)