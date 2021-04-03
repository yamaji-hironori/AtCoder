import sys
import collections
import math

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

    # Counter({3: 1, 673: 1}) - You can use this by enabling the following:
    a = collections.Counter(a)
    return a

def main():
    N, M = map(int, input().split())
    a = prime_factorize(M)
    mod = 10**9 + 7

    if len(a) == 0:
        print(1)
        return

    ans = 1
    fct = math.factorial
    for i_a in a:
        ans *= (fct(a[i_a]+N-1)//(fct(a[i_a])*fct(N-1))) % mod
        ans %= mod
    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)