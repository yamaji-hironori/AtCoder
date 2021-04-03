import sys
sys.setrecursionlimit(10**9)

def main():
    s = input()
    t = input()

    ans = 0
    for i_s, i_t in zip(s,t):
        if i_s != i_t:
            ans += 1

    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)