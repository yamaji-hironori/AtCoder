
def main():
    H, W = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(H)]
    Q = int(input())
    ABCD = [list(map(int, input().split())) for _ in range(Q)]

    X_sum = [[0]*W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            X_sum[h][w] = X[h][w]
            if h == 0 and w == 0:
                pass
            elif h == 0 and w != 0:
                X_sum[h][w] += X_sum[h][w-1]
            elif h != 0 and w == 0:
                X_sum[h][w] += X_sum[h-1][w]
            elif h != 0 and w != 0:
                X_sum[h][w] += X_sum[h][w-1] + (X_sum[h-1][w] - X_sum[h-1][w-1])

    for a, b, c, d in ABCD:
        a, b, c, d = map(lambda x: x-1, [a, b, c, d])
        ans = X_sum[c][d]
        if a == 0 and b == 0:
            pass
        elif a == 0 and b != 0:
            ans -= X_sum[c][b-1]
        elif a != 0 and b == 0:
            ans -= X_sum[a-1][d]
        elif a != 0 and b != 0:
            ans -= X_sum[c][b-1] + X_sum[a-1][d] - X_sum[a-1][b-1]
        print(ans)


if __name__ == '__main__':
    main()
