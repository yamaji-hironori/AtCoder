import sys

def main():
    A, B, C, K = map(int, input().split())

    ans = 0
    if A >= K:
        ans += K
        print(ans)
        return
    else:
        ans += A
        K -= A

    if B >= K:
        print(ans)
        return
    else:
        K -= B
    
    if C >= K:
        ans -= K
        print(ans)
        return
    else:
        ans -= C
        print(ans)

    return


if __name__ == "__main__":
    main()
    sys.exit(0)