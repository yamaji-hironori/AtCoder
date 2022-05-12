from pprint import pprint # type: ignore
import sys
sys.setrecursionlimit(10**9)
from typing import Dict, List, Tuple, Union #type: ignore

def calculate(a: int, b: int) -> int:
    return a**3 + a**2*b + a*b**2 + b**3

def binary_search(left: int, right: int, a: int, N: int) -> int:
    if right < left:
        return calculate(a, left)
    middle = (left + right) // 2
    i_X = calculate(a, middle)
    i_min_X = float('inf')
    if i_X == N:
        return i_X
    elif i_X < N:
        left = middle + 1
        i_min_X = binary_search(left, right, a, N)
    else:
        right = middle - 1
        i_min_X = binary_search(left, right, a, N)

    return i_min_X

def main() -> None:
    N = int(input())
    a = 10**6
    min_X: Union[int, float] = float('inf')
    while a >= 0:
        i_min_X = binary_search(0, a, a, N)
        if N <= i_min_X: min_X = min(min_X, i_min_X)
        a -= 1

    print(min_X)
    return


if __name__ == "__main__":
    main()
