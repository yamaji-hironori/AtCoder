import sys

def main():
    N = int(input())
    A = [input() for i in range(N)]

    # index '0' is not using.
    A.insert(0, None)
    half_ans = ''
    for i in range(1, N//2+1):
        for i_A in A[i]:
            if i_A in A[N-i+1]:
                half_ans += i_A
                break
        else:
            print(-1)
            return

    if N % 2 == 0:
        ans = half_ans + half_ans[::-1]
    else:
        ans = half_ans + A[N//2+1][0] + half_ans[::-1]

    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)