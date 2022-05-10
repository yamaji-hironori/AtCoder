import sys
sys.setrecursionlimit(10**9)


def main():
    h,w = map(int, input().split())
    r,c = map(int, input().split())

    tate = 0
    yoko = 0

    if h == 1:
        tate = 0
    elif 1 == r or h == r:
        tate = 1
    else:
        tate = 2

    if w == 1:
        yoko = 0
    elif 1 == c or w == c:
        yoko = 1
    else:
        yoko = 2

    print(yoko + tate)
    return


if __name__ == "__main__":
    main()
