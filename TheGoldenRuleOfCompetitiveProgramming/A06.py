from typing import List, Tuple

def main():
    _, Q = map(int, input().split())
    A = [int(_) for _ in input().split()]
    LR: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(Q)]

    # 累積和を求める
    A_sum: List[int] = []
    for i in range(len(A)):
        A_sum.append(A[i] + A_sum[i-1] if i != 0 else A[i])

    for lr in LR:
        l, r = lr
        r_idx = r - 1 # 要素番号を考慮し -1
        l_idx = l - 2 # 要素番号を考慮し -1、前日までの合計値を引くため -1
        ans = A_sum[r_idx] - A_sum[l_idx] if l != 1 else A_sum[r_idx]
        print(ans)


if __name__ == '__main__':
    main()
