
def main() -> None:
    N = int(input())
    S = [input() for _ in range(N)]
    s = set(S)
    print(len(s))

if __name__ == '__main__':
    main()
    exit()
