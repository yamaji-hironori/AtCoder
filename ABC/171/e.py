import sys
sys.setrecursionlimit(10**9)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    total = 0
    for i_a in a:
        total ^= i_a

    ans = []
    for i_a in a:
        now_ans = 0
        for i_bin in range(49):
            if i_a & (1 << i_bin) == 0:
                if total & (1 << i_bin) != 0:
                    now_ans += (1 << i_bin)
            else:
                if total & (1 << i_bin) == 0:
                    now_ans += (1 << i_bin)

        ans.append(str(now_ans))

    print(' '.join(ans))
    return


if __name__ == "__main__":
    main()
    sys.exit(0)