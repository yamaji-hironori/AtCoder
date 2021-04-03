import sys
sys.setrecursionlimit(10**9)

TO_K = []
TREE = []
DISTANCE = []

def dfs(child, parent):
    for i_node in TREE[parent]:
        if i_node[0] == child:
            TO_K[child] = TO_K[parent] + i_node[1]

    for i_gch in TREE[child]:
        if i_gch[0] == parent:
            TO_K[child] = TO_K[parent] + i_gch[1]
        else:
            dfs(i_gch[0], child)

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
    # index '0' is not used.
    TREE = [[] for _ in range(n+1)]
    for a, b, c in abc:
        TREE[a].append([b, c])
        TREE[b].append([a, c])

    dfs(k, 0)

    for x, y in xy:
        print(TO_K[x]+TO_K[y])
    return


if __name__ == "__main__":
    main()
    sys.exit(0)