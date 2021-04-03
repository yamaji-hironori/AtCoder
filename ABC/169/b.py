import sys

def main():
    n = int(input())
    A = list(map(int, input().split()))
    co = 10**18

    ans = 1

    if 0 in A:
        print(0)
        return

    for i_A in A:
        ans *= i_A
        if ans > co:
            print(-1)
            return
    
    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)