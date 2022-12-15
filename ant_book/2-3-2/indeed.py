import sys

def main():
    N, M = map(int, input().split())
    ABCW = [[int(_) for _ in input().split()] for i in range(N)]
    XYZ = [[int(_) for _ in input().split()] for i in range(M)]

    dp = [[[0]*101 for _ in range(101)] for _ in range(101)]

    for a, b, c, w in ABCW:
        dp[a][b][c] = max(dp[a][b][c], w)
    
    for a in range(101):
        for b in range(101):
            for c in range(101):
                dp[a][b][c] = max(dp[a][b][c], dp[max(0,a-1)][b][c], \
                                  dp[a][max(0,b-1)][c], dp[a][b][max(0,c-1)])

    for x, y, z in XYZ:
        print(dp[x][y][z])

    return


if __name__ == "__main__":
    main()
    sys.exit(0)