import sys
sys.setrecursionlimit(10**9)

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    p.sort()
    ans = sum(p[:k])
    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)