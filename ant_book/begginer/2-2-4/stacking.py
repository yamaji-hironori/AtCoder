N = int(input())
Cardboard= [int(input()) for i in range(N)]

stacking_list = [[Cardboard[0]]]
for i_box_weight in Cardboard[1:]:

    min_diff_weight_box = 10**5 + 1
    min_diff_pos = 51
    for j_pos, j_stacking_list in enumerate(stacking_list):

        now_diff_weight = j_stacking_list[-1] - i_box_weight
        if i_box_weight <= j_stacking_list[-1] and \
                                         now_diff_weight <= min_diff_weight_box:
            min_diff_weight_box = now_diff_weight
            min_diff_pos = j_pos
    
    if min_diff_pos == 51:
        stacking_list.append([i_box_weight])
        continue
    
    else:
        stacking_list[min_diff_pos].append(i_box_weight)

print(len(stacking_list))
exit()