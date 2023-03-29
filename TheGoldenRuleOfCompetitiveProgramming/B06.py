from typing import List

def main() -> None:
    _ = int(input())
    Ai = list(map(int, input().split()))
    Q = int(input())
    hits: List[int] = []
    for i in range(len(Ai)):
        i_a = 1 if Ai[i] == 1 else -1
        hits.append(hits[i - 1] + i_a if i != 0 else i_a)

    for _ in range(Q):
        l, r = map(int, input().split())
        ans = hits[r - 1] - hits[l - 2] if l > 1 else hits[r-1]
        if ans > 0: print('win')
        elif ans < 0: print('lose')
        else: print('draw')


if __name__ == '__main__':
    main()
