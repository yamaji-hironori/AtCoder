import sys
import collections

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

def main():
    N = int(input())
    
    fct = prime_factorize(N)
    ans = 0
    for i_fct in fct:
        m = fct[i_fct]
        if m == 1:
            ans += 1
            continue

        sum = 0
        add = 1
        while True:
            sum += add
            if sum > m:
                break
            add += 1
            ans += 1

    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)