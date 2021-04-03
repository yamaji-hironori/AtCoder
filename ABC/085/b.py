import sys
sys.setrecursionlimit(10**9)

def main():
    n = int(input())
    d = [int(input()) for i in range(n)]
    d = set(d)

    print(len(d))
    return


if __name__ == "__main__":
    main()
    sys.exit(0)