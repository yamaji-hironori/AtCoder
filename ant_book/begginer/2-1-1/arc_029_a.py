N = int(input())
T_list = [int(input()) for _ in range(N)]

min_time = 210
for i_binary in range(2**N):
    first_machine_time = 0
    second_machine_time = 0

    for i_position in range(N):
        if (i_binary >> i_position) & 1 == 1:
            first_machine_time += T_list[i_position]
        else:
            second_machine_time += T_list[i_position]
    
    longer_time = max(first_machine_time, second_machine_time)
    min_time = min(min_time, longer_time)

print(min_time)