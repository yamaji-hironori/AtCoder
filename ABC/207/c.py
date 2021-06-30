
def main():
    N = int(input())
    tlr = [list(map(int, input().split())) for _ in range(N)]
    span_max = float('inf')
    span_min = -float('inf')

    for t, l, r in tlr:
        if t == 1:
            pass
        elif t == 2:
            r -= 1
        elif t == 3:
            l += 1
        elif t == 4:
            l += 1
            r -= 1
        else:
            raise
        span_max = min(span_max, r)
        span_min = max(span_min, l)

    print(span_min, span_max)
    if span_min > span_max:
        ans = 0
    else:
        ans = span_max - span_min

    print(ans)

if __name__ == '__main__':
    main()
