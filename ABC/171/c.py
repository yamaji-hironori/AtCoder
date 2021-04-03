import sys
sys.setrecursionlimit(10**9)

def main():
    n = int(input())
    compare = [1]
    total = 1
    for i in range(1, 11):
        now = 26**i
        total = total+now
        if n < total:
            break
        compare.append(now)
    ans = ''
    n -= sum(compare)
    for i_compare in compare[::-1]:
        q, mod = divmod(n, i_compare)
        ans += chr(97+q)
        n = mod

    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)