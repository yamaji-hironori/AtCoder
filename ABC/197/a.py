import sys

def main() -> None:
    s = input()
    ans = s[1:] + s[0]
    print(ans)

if __name__ == '__main__':
    main()
    sys.exit()