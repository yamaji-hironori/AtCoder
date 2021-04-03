import sys


def main():
    N = int(input())
    A_list = list(map(int, input().split()))

    ans = 'APPROVED'
    for i_A in A_list:
        if i_A % 2 == 1:
            continue

        if i_A % 3 != 0 and i_A % 5 != 0:
            ans = 'DENIED'

    print(ans)

    return


if __name__ == "__main__":
    main()
    sys.exit(0)