import sys
import copy
from collections import deque


def main():
    N, M, Q = map(int, input().split())
    ABCD = [[int(_) for _ in input().split()] for i in range(Q)]

    seq_list = make_sequence(N, M)
    
    max_score = 0
    for i_seq in seq_list:
        score = 0
        for a, b, c, d in ABCD:
            if (i_seq[b-1] - i_seq[a-1]) == c:
                score += d
        
        max_score = max(max_score, score)

    print(max_score)
    return


def make_sequence(N, M):
    seq_list = []
    sequence = [-1] * N

    seq_deque = deque()
    now_ele = 0
    for i in range(M):
        sequence[0] = i
        now_seq = copy.copy(sequence)
        seq_deque.append([now_ele, now_seq])

    while len(seq_deque) > 0:
        pre_ele ,pre_seq = seq_deque.popleft()
        if pre_seq[-1] != -1:
            seq_list.append(pre_seq)
            continue

        end_ele = M - sum(pre_seq[0:pre_ele+1])
        for i in range(end_ele):
            pre_seq[pre_ele+1] = i
            now_seq = copy.copy(pre_seq)
            seq_deque.append([pre_ele+1 ,now_seq])

    for i_seq in seq_list:
        now_value = 1
        for i, i_value in enumerate(i_seq):
            now_value += i_value
            i_seq[i] = now_value

    return seq_list


if __name__ == '__main__':
    main()
    sys.exit(0)