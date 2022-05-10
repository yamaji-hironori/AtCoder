import sys
sys.setrecursionlimit(10**9)

from typing import List
def sieve_of_eratosthenes(n: int) -> List[bool]:
    import math
    prime = [True for _ in range(n+1)]
    prime[0] = False
    prime[1] = False
    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    return prime

def get_seg_prime():
    n = 10**6
    # 素数の列挙
    prime = sieve_of_eratosthenes(n)
    tmp = []
    for p in range(n+1):
        if prime[p]:
            tmp.append(p)
    return tmp

def main():
    N = int(input())
    ans = 0
    seg_prime = get_seg_prime()
    max_i = len(seg_prime) - 1
    for i, i_prime in enumerate(seg_prime):
        if i_prime**3 >= N:
            max_i = i
            break

    j_p = 0
    for i_q in range(max_i, -1, -1):
        if i_q <= j_p:
            ans += (i_q+1) -1
            continue
        q = seg_prime[i_q]
        ans_flg = False
        for j in range(j_p, i_q):
            p = seg_prime[j]
            if p*q**3 <=N:
                ans_flg = True
                j_p = j
            else:
                break

        if ans_flg:
            ans += j_p+1

    print(ans)
    return


if __name__ == "__main__":
    main()
