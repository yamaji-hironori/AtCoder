import sys
import bisect

def main():
    N = int(input())
    WH = [[int(_) for _ in input().split()] for i in range(N)]
    INF = float('inf')

    WH.sort(key=lambda x: (x[0],-x[1]))
    dp = [INF]*(N+2)
    dp[0] = -INF

    for _, i_h in WH:
        insert_index = bisect.bisect_left(dp, i_h)
        dp[insert_index] = i_h

    for i in range(1, N+2):
        if dp[i] == INF:
            ans = i-1
            break

    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)