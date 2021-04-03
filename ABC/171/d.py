import sys
sys.setrecursionlimit(10**9)
import collections

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [[int(_) for _ in input().split()] for i in range(q)]

    ans = sum(a)
    a = collections.Counter(a)
    for b, c in bc:
        if b not in a:
            print(ans)
            continue
        b_num = a[b]
        ans -= b_num * b
        ans += b_num * c
        if c in a:
            a[c] += b_num
        else:
            a[c] = b_num
        a[b] = 0
        print(ans)

    return


if __name__ == "__main__":
    main()
    sys.exit(0)