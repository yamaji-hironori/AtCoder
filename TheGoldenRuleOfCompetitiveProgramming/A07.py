
def main() -> None:
    D = int(input())
    days = [0] * D
    N = int(input())
    LR = [tuple(map(int, input().split())) for _ in range(N)]
    for lr in LR:
        l, r = lr
        days[l-1] += 1
        if r != D: days[r] -= 1

    ans = 0
    for d in days:
        ans += d
        print(ans)


if __name__ == '__main__':
    main()
