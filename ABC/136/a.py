import sys

def main():
    A, B, C = map(int, input().split())
    ans = max(0, C - (A-B))
    print(ans)

    return


if __name__ == '__main__':
    main()
    sys.exit(0)