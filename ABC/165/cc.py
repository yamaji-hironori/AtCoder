import sys
import itertools

def main():
    N, M, Q = map(int, input().split())
    ABCD = [[int(_) for _ in input().split()] for i in range(Q)]
    value_range = list(range(1, M+1))
    seq_list = list(itertools.combinations_with_replacement(value_range, N))

    max_score = 0
    for i_seq in seq_list:
        score = 0
        for a, b, c, d in ABCD:
            if (i_seq[b-1] - i_seq[a-1]) == c:
                score += d

        max_score = max(max_score, score)

    print(max_score)
    return

if __name__ == '__main__':
    main()
    sys.exit(0)