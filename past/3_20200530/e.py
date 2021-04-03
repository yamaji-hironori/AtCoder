import sys

def main():
    N, M, Q = map(int, input().split())
    UV = [[int(_) for _ in input().split()] for i in range(M)]
    C = list(map(int, input().split()))
    S = [[int(_) for _ in input().split()] for i in range(Q)]

    # index '0' is not using.
    graph = [[] for _ in range(N+1)]
    for i_u, i_v in UV:
        graph[i_u].append(i_v)
        graph[i_v].append(i_u)

    # index '0' is not using.
    color = [None]*(N+1)
    for i, i_C in enumerate(C, 1):
        color[i] = i_C

    for i_S in S:
        if i_S[0] == 1:
            print(color[i_S[1]])
            for i_graph in graph[i_S[1]]:
                color[i_graph] = color[i_S[1]]

        else:
            print(color[i_S[1]])
            color[i_S[1]] = i_S[2]

    return


if __name__ == "__main__":
    main()
    sys.exit(0)