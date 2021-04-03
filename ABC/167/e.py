import sys
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

def main():
    N, M, K = map(int, input().split())
    mod = 998244353

    if M == 1:
        print(1)
        return
    elif N == 1:
        print(M)
        return

    ans = 0
    for i_K in range(K+1):
        combinations = combinations_count(N, i_K)
        now_repeat = N - i_K
        now_num = (M * ((M-1)** (now_repeat//2))) % mod
        now_num = (now_num * combinations) % mod
        '''
        if now_repeat == 1:
            ans = (ans + M) % mod
            continue
        if now_repeat % 2 == 0:
            now_num = (now_num ** (now_repeat//2)) % mod
            now_num = (now_num * num_stick) % mod
        else:
            now_num = (now_num ** (now_repeat//2)) % mod
            now_num = (now_num*(M-1)) % mod
        ans = (ans + now_num) % mod
        '''

    print(now_num)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)