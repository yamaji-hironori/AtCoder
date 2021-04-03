import sys

def main():
    N, A, B = map(int, input().split())

    A = N * A

    if A < B:
        print(A)
    else:
        print(B)

    return


if __name__ == "__main__":
    main()
    sys.exit(0)