from pprint import pprint # type: ignore
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

def get_prime_numbers() -> List[int]:
    prime_numbers: List[int] = []
    primes = sieve_of_eratosthenes(10**6)
    for i, i_prime in enumerate(primes):
        if i_prime:
            prime_numbers.append(i)
    return prime_numbers

def main() -> None:
    N = int(input())
    prime_numbers = get_prime_numbers()
    ans = 0
    keep_p_pos = 0
    for i, q in enumerate(reversed(prime_numbers)):
        if N < q**3: continue
        if q <= prime_numbers[keep_p_pos]:
            ans += len(prime_numbers) - (i+1)
            continue

        exist_or_less_N = False
        for p_pos in range(keep_p_pos, len(prime_numbers)+1):
            p = prime_numbers[p_pos]
            if q <= p:
                break
            elif p*q**3 <= N:
                keep_p_pos = p_pos
                exist_or_less_N = True
            else:
                break

        if exist_or_less_N: ans += keep_p_pos+1

    print(ans)
    return

if __name__ == "__main__":
    main()
