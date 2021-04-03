from collections import deque

N = int(input())
P = list(map(int, input().split()))

score_list = [0]
for i_p in P:

    next_score_list = deque()
    for i_score in score_list:
        next_score_list.append(i_score)
        next_score_list.append(i_score+i_p)

    score_list = list(set(next_score_list))

print(len(score_list))