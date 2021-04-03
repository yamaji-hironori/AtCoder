import sys
sys.setrecursionlimit(10**9)


def main():
    n = int(input())
    abc = [[int(_) for _ in input().split()] for i in range(n-1)]
    q, k = map(int, input().split())
    xy = [[int(_) for _ in input().split()] for i in range(q)]

    # index '0' is not used.
    to_k = [-1]*(n+1)

    # index '0' is not used.
    tree = [[] for _ in range(n+1)]
    for a, b, c in abc:
        tree[a].append([b, c])
        tree[b].append([a, c])

    def dfs(parent, distance):
        for i_node in tree[parent]:
            child, dd = i_node
            if to_k[child] != -1:
                continue

            next_dt = distance + dd
            to_k[child] = next_dt
            dfs(child, next_dt)

        return

    to_k[k] = 0
    dfs(k, 0)

    for x, y in xy:
        print(to_k[x]+to_k[y])
    return


if __name__ == "__main__":
    main()
    sys.exit(0)