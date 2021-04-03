import sys
sys.setrecursionlimit(10**9)

def main():
    H, W, M = list(map(int, input().split()))
    hw = [[int(_) for _ in input().split()] for i in range(M)]

    # Do not use element '0'.
    x_map = [0]*(3*10**5+1)
    y_map = [0]*(3*10**5+1)

    for h, w in hw:
        x_map[w] += 1
        y_map[h] += 1

    max_x = max(x_map)
    max_y = max(y_map)

    ans = x_map[max_x] + y_map[max_y]

    if (max_y, max_x) in hw:
        ans -= 1

    print(ans)
    return


if __name__ == "__main__":
    main()
