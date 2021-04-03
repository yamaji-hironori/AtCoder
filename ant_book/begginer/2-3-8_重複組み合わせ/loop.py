import sys
import math

def main():
    N = int(input())
    K = int(input())
    mod = 1000000007

    fct = math.factorial

    fct1 = fct(N+K-1)
    fct2 = fct(N-1)
    fct3 = fct(K)
    ans = (fct1 // (fct2*fct3)) % mod
    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)