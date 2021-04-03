N, K, C = map(int, input().split())
S = input()
S_reverse = S[::-1]

left_justified = [-1 for _ in range(N)]
right_justified = [-2 for _ in range(N)]

for i_justified in (left_justified, right_justified):
    if i_justified == left_justified:
        i_S = S
        nearest_position = 1
        positioning = 1
    else:
        i_S = S_reverse
        nearest_position = K
        positioning = -1
    
    i_K = 0
    
    while i_K <= N-1:
        if i_S[i_K] == 'o':
            i_justified[i_K] = nearest_position
            i_K += C
            nearest_position += positioning
        i_K += 1

for i_N in range(N):
    if left_justified[i_N] == right_justified[N - i_N - 1]:
        print(i_N + 1)