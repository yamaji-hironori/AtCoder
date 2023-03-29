
def main() -> None:
    T = int(input())
    hours = [0] * T
    N = int(input())
    LR = [tuple(map(int, input().split())) for _ in range(N)]
    for lr in LR:
        l, r = lr
        hours[l] += 1
        if r != T: hours[r] -= 1

    ans = 0
    for h in hours:
        ans += h
        print(ans)


if __name__ == '__main__':
    main()
