d, g = map(int, input().split())
pc = [[int(_) for _ in input().split()] for i in range(d)]

min_problem = 1100
for i_num in range(2 ** d):
    score = 0
    num_problem = 0
    for i_pos in range(d):
        if (i_num >> i_pos) & 1 == 0:
            continue
        score += pc[d-i_pos-1][1] + (d-i_pos)*100*pc[d-i_pos-1][0]
        num_problem += pc[d-i_pos-1][0]
    
    if score < g:
        for j_pos in range(d):
            if (i_num >> j_pos) & 1 == 0:
                add_position = d-j_pos-1
                break
        for j_problem_ammount in range(1, pc[add_position][0]):
            add_score = score + (add_position+1)*100*j_problem_ammount
            if add_score >= g:
                min_problem = min(min_problem, num_problem+j_problem_ammount)
                break
    else:
        min_problem = min(min_problem, num_problem)

print(min_problem)