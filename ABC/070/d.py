import sys

TO_K = []
TREE = []
DISTANCE = []

def dfs(child, parent):
    TO_K[child] = TO_K[parent] + DISTANCE[parent][child]

    for i_gch in TREE[child]:
        if i_gch == parent:
            continue
        dfs(i_gch, child)

    return


def main():
    n = int(input())
    abc = [[int(_) for _ in input().split()] for i in range(n-1)]
    q, k = map(int, input().split())
    xy = [[int(_) for _ in input().split()] for i in range(q)]

    global TO_K
    # index '0' is not used.
    TO_K = [0]*(n+1)

    global TREE
    global DISTANCE
    # index '0' is not used.
    TREE = [[] for _ in range(n+1)]
    DISTANCE = [[0]*(n+1) for _ in range(n+1)]
    for a, b, c in abc:
        TREE[a].append(b)
        TREE[b].append(a)
        DISTANCE[a][b] = c
        DISTANCE[b][a] = c

    dfs(k, 0)

    for x, y in xy:
        print(TO_K[x]+TO_K[y])
    return


if __name__ == "__main__":
    main()
    sys.exit(0)