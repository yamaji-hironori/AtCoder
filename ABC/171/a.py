import sys
sys.setrecursionlimit(10**9)

def main():
    n = input()

    if n.islower():
        print('a')
    else:
        print('A')
    return


if __name__ == "__main__":
    main()
    sys.exit(0)