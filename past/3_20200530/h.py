import sys

def main():
    N, L = map(int, input().split())
    X = list(map(int, input().split()))
    T = list(map(int, input().split()))

    dp = [float('inf')]*(L+1)
    dp[0] = 0

    obstacle = [False]*(L+1)
    for i_X in X:
        obstacle[i_X] = True

    for i in range(L):
        crc = 0
        if obstacle[i]:
            crc = T[2]

        dp[i+1] = min(dp[i+1], dp[i]+T[0]+crc)

        if i+2 > L:
            dp[i+1] = min(dp[i+1], dp[i]+T[0]//2+T[1]//2+crc)
        else:
            dp[i+2] = min(dp[i+2], dp[i]+T[0]+T[1]+crc)

        if i+2 > L:
            pass
        elif i+3 > L:
            dp[i+2] = min(dp[i+2], dp[i]+T[0]//2+T[1]+T[1]//2+crc)
        elif i+4 > L:
            dp[i+3] = min(dp[i+3], dp[i]+T[0]//2+2*T[1]+T[1]//2+crc)
        else:
            dp[i+4] = min(dp[i+4], dp[i]+T[0]+3*T[1]+crc)

    print(dp[-1])
    return


if __name__ == "__main__":
    main()
    sys.exit(0)