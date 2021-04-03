import sys

def main():
    A, B, N = map(int, input().split())

    if B == 1:
        ans = 0
        print(ans)
        return

    if B > N:
        x = N
    else:
        x = B-1

    ans = (A*x) // B
    print(ans)
    return

if __name__ == '__main__':
    main()
    sys.exit(0)