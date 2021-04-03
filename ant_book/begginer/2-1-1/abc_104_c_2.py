Amount_problem, Goal_point = map(int, input().split())
NumPro_ConpBonus = [[int(_) for _ in input().split()] for i in range(Amount_problem)]

min_num_ans = 1100
for i_binary in range(2**Amount_problem):
    num_ans = 0
    now_point = 0

    # Set highest scoring question to minimum position.
    for i_position in range(Amount_problem):
        if (i_binary >> i_position) & 1 == 0:
            continue

        now_point += NumPro_ConpBonus[(Amount_problem-1) - i_position][1] \
            + 100*(Amount_problem-i_position)*NumPro_ConpBonus[(Amount_problem-1) - i_position][0]

        num_ans += NumPro_ConpBonus[(Amount_problem-1) - i_position][0]

    if now_point < Goal_point:
        for i_position in range(Amount_problem):
            if (i_binary >> i_position) & 1 == 1:
                continue

            for add_num_ans in range(1, NumPro_ConpBonus[(Amount_problem-1) - i_position][0]):
                if (now_point + 100*(Amount_problem-i_position)*add_num_ans) >= Goal_point:
                    min_num_ans = min(min_num_ans, num_ans+add_num_ans)
                    break
    else:
        min_num_ans = min(min_num_ans, num_ans)

print(min_num_ans)