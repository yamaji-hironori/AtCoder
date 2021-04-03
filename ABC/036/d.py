import sys

MOD = 10**9 + 7
ISLANDS = []

def dfs(child, parent):
    white, black = 1, 1
    if ISLANDS[child][0] == parent and len(ISLANDS[child]) == 1:
        return white, black

    for i_gch in ISLANDS[child]:
        if i_gch == parent:
            continue

        i_white, i_black = dfs(i_gch, child)
        white *= i_white + i_black
        black *= i_white

    white %= MOD
    black %= MOD
    return white, black

def main():
    global ISLANDS
    n = int(input())
    ab = [[int(_) for _ in input().split()] for i in range(n-1)]

    # index '0' is not used.
    ISLANDS = [[] for _ in range(n+1)]
    for a, b in ab:
        ISLANDS[a].append(b)
        ISLANDS[b].append(a)

    white, black = dfs(1, 0)
    ans = (white+black) % MOD
    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)