import sys
sys.setrecursionlimit(10**9)

def main():
    n, k, l = map(int, input().split())
    pq = [[int(_) for _ in input().split()] for i in range(k)]
    rs = [[int(_) for _ in input().split()] for i in range(l)]

    # index '0' is not used.
    road = [[] for _ in range(n+1)]
    train = [[] for _ in range(n+1)]
    
    for p, q in pq:
        road[p].append(q)
        road[q].append(p)

    for r, s in rs:
        train[r].append(s)
        train[s].append(r)

    ans = []
    for i in range(1, n+1):
        if len(road[i]) != 0 and len(train[i]) != 0:
            now = 2
        else:
            now = 1
        ans.append(str(now))

    print(' '.join(ans))
    return


if __name__ == "__main__":
    main()
    sys.exit(0)