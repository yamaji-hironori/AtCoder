import sys
sys.setrecursionlimit(10**9)

NEGA = 0
POSI = 1
EVEN = 0
ODD = 1
MOD = 10**9 + 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    is_all_nega = True

    b = []
    for i_a in a:
        if i_a < 0:
            b.append((abs(i_a), NEGA))
        else:
            b.append((i_a, POSI))
            is_all_nega = False

    a.sort(reverse=True)
    ans = 1
    if is_all_nega and k % 2 == 1:
        for i in range(k):
            ans *= a[i]
            ans %= MOD
        print(ans)
        return


    b.sort(reverse=True)

    e_or_o = 0
    pool_nega_num = None
    pool_posi_num = None
    add_num = 0
    ans = 1
    for i_num, i_n_or_p in b:
        if i_n_or_p == NEGA:
            e_or_o += 1

            if e_or_o % 2 == 0:
                if add_num + 1 == k:
                    if pool_posi_num is None:
                        ans *= i_num * pool_nega_num
                    else:
                        ans = ans * i_num * pool_nega_num // pool_posi_num
                    ans %= MOD
                    add_num += 1
                else:
                    ans *= i_num * pool_nega_num
                    ans %= MOD
                    add_num += 2
            else:
                pool_nega_num = i_num
        
        else:
            ans *= i_num
            ans %= MOD
            add_num += 1
            pool_posi_num = i_num

        if add_num == k:
            break

    if e_or_o % 2 == 1:
        ans *= -1
        ans %= MOD
    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)