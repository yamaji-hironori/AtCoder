
def main():
    N = int(input())
    l = [0] * N
    r = [0] * N

    for i in range(N):
        t, l[i], r[i] = map(int, input().split())
        if t == 1:
            pass
        elif t == 2:
            r[i] -= 0.5
        elif t == 3:
            l[i] += 0.5
        elif t == 4:
            l[i] += 0.5
            r[i] -= 0.5
        else:
            raise

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if max(l[i], l[j]) <= min(r[i], r[j]):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
