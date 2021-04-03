import sys
sys.setrecursionlimit(10**9)

TO_K = []
TREE = []

def dfs(parent, distance):
    for i_node in TREE[parent]:
        child, dd = i_node
        if TO_K[child] != -1:
            continue

        next_dt = distance + dd
        TO_K[child] = next_dt
        dfs(child, next_dt)

    return


def main():
    n = int(input())
    abc = [[int(_) for _ in input().split()] for i in range(n-1)]
    q, k = map(int, input().split())
    xy = [[int(_) for _ in input().split()] for i in range(q)]

    global TO_K
    # index '0' is not used.
    TO_K = [-1]*(n+1)

    global TREE
    # index '0' is not used.
    TREE = [[] for _ in range(n+1)]
    for a, b, c in abc:
        TREE[a].append([b, c])
        TREE[b].append([a, c])

    TO_K[k] = 0
    dfs(k, 0)

    for x, y in xy:
        print(TO_K[x]+TO_K[y])
    return


if __name__ == "__main__":
    main()
    sys.exit(0)