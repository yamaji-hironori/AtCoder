import sys
sys.setrecursionlimit(10**9)

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.insert(0, 0)
    b.insert(0, 0)

    a_sum = [0]*(n+1)
    a_sum[0] = a[0]
    for i in range(1, n+1):
        a_sum[i] = a_sum[i-1] + a[i]

    b_sum = [0]*(m+1)
    b_sum[0] = b[0]
    for i in range(1, m+1):
        b_sum[i] = b_sum[i-1] + b[i]

    b_sum = b_sum[::-1]

    i_b = 0
    ans = 0
    for i_a in range(n+1):
        while i_b <= m:
            if k < a_sum[i_a] + b_sum[i_b]:
                i_b += 1
                continue
            else:
                ans = max(ans, i_a+(m-i_b))
                break

    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)