import sys
sys.setrecursionlimit(10**9)

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    ans = 0

    for i in range(0, n-1):
        now_index = (i+1) // 2
        ans += a[now_index]

    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)
