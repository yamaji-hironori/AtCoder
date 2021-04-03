import sys

def main():
    S = input()
    T = input()

    if S == T:
        ans = 'same'
    elif S.lower() == T.lower():
        ans = 'case-insensitive'
    else:
        ans = 'different'

    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)