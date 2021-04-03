import sys
sys.setrecursionlimit(10**9)

def main():
    a = int(input())
    ans = a + a**2 + a**3

    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)