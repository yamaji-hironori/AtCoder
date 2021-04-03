import sys
sys.setrecursionlimit(10**9)
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

def main():
    k = int(input())
    s = len(input())
    mod = 10**9 + 7

    ans = 0
    for i in range(k+1):
        now = 0
        now = pow(26,k-i,mod)
        now %= mod

        now *= pow(25,i,mod) 
        now %= mod
        now *= combinations_count(s+i-1, s-1)
        now %= mod

        ans += now
        ans %= mod

    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)