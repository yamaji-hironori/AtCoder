import sys
sys.setrecursionlimit(10**9)

def main():
    n, x, t = map(int, input().split())
    if n % x == 0:
        print((n//x)*t)
    else:
        print((n//x+1)*t)
    return


if __name__ == "__main__":
    main()
