import sys

def main():
    N, Z, W = map(int, input().split())
    A = list(map(int, input().split()))

    if len(A) == 1:
        ans = abs(A[0] - W)
    else:
        ans = max(abs(A[-1]-W), abs(A[-2]-A[-1]))

    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)