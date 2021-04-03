import sys

def main():
    A, R, N = map(int, input().split())

    ans = A
    for _ in range(1, N):
        ans *= R
        if ans > 10**9:
            print('large')
            break
    else:
        print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)