import sys
import  collections

def main():
    N, D = map(int, input().split())

    prime_factor = prime_factorize(D)
    factor_a, factor_b, factor_c = 0, 0, 0
    for key, value in prime_factor.items():
        if key == 2:
            factor_a = value
        elif key == 3:
            factor_b = value
        elif key == 5:
            factor_c = value
        else:
            print(0)
            return

    dp = [[[[0 for _ in range(factor_c+1)] for _ in range(factor_b+1)] \
                                for _ in range(factor_a+1)] for _ in range(N+1)]
    dp[0][0][0][0] = 1
    for i_N in range(N):
        for i_a in range(factor_a+1):
            for i_b in range(factor_b+1):
                for i_c in range(factor_c+1):
                    # When the die is 1.
                    dp[i_N+1][i_a][i_b][i_c] += dp[i_N][i_a][i_b][i_c] / 6
                    # When the die is 2.
                    dp[i_N+1][min(i_a+1,factor_a)][i_b][i_c] += \
                                                      dp[i_N][i_a][i_b][i_c] / 6
                    # When the die is 3.
                    dp[i_N+1][i_a][min(i_b+1, factor_b)][i_c] += \
                                                      dp[i_N][i_a][i_b][i_c] / 6
                    # When the die is 4.
                    dp[i_N+1][min(i_a+2, factor_a)][i_b][i_c] += \
                                                      dp[i_N][i_a][i_b][i_c] / 6
                    # When the die is 5.
                    dp[i_N+1][i_a][i_b][min(i_c+1, factor_c)] += \
                                                      dp[i_N][i_a][i_b][i_c] / 6
                    # When the die is 6.
                    dp[i_N+1][min(i_a+1,factor_a)][min(i_b+1,factor_b)][i_c] +=\
                                                      dp[i_N][i_a][i_b][i_c] / 6


    print(dp[N][factor_a][factor_b][factor_c])

    return

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2

    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    
    if n != 1:
        a.append(n)
    
    a = collections.Counter(a)
    return a

if __name__ == "__main__":
    main()
    sys.exit(0)