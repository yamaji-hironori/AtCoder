import sys

def main():
    N, K = map(int, input().split())

    sunuke = []
    for _ in range(K):
        _ = input()
        next_sunuke = list(map(int, input().split()))
        for i in next_sunuke:
            sunuke.append(i)
    sunuke = set(sunuke)

    print(N - len(sunuke))

    return

if __name__ == '__main__':
    main()
    sys.exit(0)