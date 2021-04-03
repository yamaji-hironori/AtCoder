import sys
sys.setrecursionlimit(10**7)

H, W = map(int, input().split())
A = [[int(_) for _ in input().split()] for i in range(H)]
PATH_CNT = [[-1]*W for _ in range(H)]
MOD = 10**9 + 7

def dfs(y, x):
    if PATH_CNT[y][x] != -1:
        return PATH_CNT[y][x]

    now_path_cnt = 1
    for dy, dx in [(0,-1), (-1,0), (0,1), (1,0)]:
        y_next, x_next = y+dy, x+dx
        if (y_next <= -1 or H <= y_next) or (x_next <= -1 or W <= x_next):
            continue
        
        if A[y][x] < A[y_next][x_next]:
            now_path_cnt += dfs(y_next, x_next)

    PATH_CNT[y][x] = now_path_cnt % MOD
    return now_path_cnt


def main():
    ans = 0
    for y in range(H):
        for x in range(W):
            if PATH_CNT[y][x] == -1:
                dfs(y, x)
            ans += PATH_CNT[y][x]
            ans %= MOD

    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)