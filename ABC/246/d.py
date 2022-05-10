import math
import sys
from typing import Union
sys.setrecursionlimit(10**9)

min_x = math.inf
N = int(input())

def calc_x(a: int, b: int) -> int:
    return a**3 + a**2 * b + a * b**2 + b**3

def binaly_search(a: int, left: int, right: int) -> Union[int, float]:
    if right < left:
        return calc_x(a, left)
    middle = (left + right) // 2
    now_x = calc_x(a, middle)
    if now_x == N:
        return now_x
    elif now_x < N:
        left = middle + 1
        match_x = binaly_search(a, left, right)
    elif now_x > N:
        right = middle - 1
        match_x = binaly_search(a, left, right)
    else:
        raise Exception('unexpected')
    return match_x

def main():
    a = 10 ** 6
    global min_x
    for i in range(a+1):
        now_x = binaly_search(i, 0, i)
        if (now_x >= N): min_x = min(min_x, now_x)
    print(min_x)
    return

if __name__ == "__main__":
    main()
