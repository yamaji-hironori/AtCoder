import sys

def main():
    A, B = map(int, input().split())
    ab = abs(A+B)
    if ab % 2 == 1:
        print('IMPOSSIBLE')
    else:
        print(ab // 2)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)