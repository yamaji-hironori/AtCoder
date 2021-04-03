import sys
sys.setrecursionlimit(10**9)
import collections

def main():
    n = int(input())
    s = [input() for i in range(n)]
    m = int(input())
    t = [input() for i in range(m)]

    s = collections.Counter(s)
    t = collections.Counter(t)

    ans = 0
    for key, value in s.items():
        if key in t:
            ans = max(ans, value-t[key])
        else:
            ans = max(ans, value)

    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)