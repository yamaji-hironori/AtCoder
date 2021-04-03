NumString = int(input())
String = input()

r_string_num, g_string_num, b_string_num = 0, 0, 0
for i_string in String:
    if i_string == 'R':
        r_string_num += 1
    elif i_string == 'G':
        g_string_num += 1
    else:
        b_string_num += 1
    
total_ans = r_string_num * g_string_num * b_string_num

exclude_num = 0
for i in range(NumString-2):
    for j in range(i+1, NumString-1):
        if (2*j - i) < NumString and String[i] != String[j] and \
            String[j] != String[2*j-i] and String[i] != String[2*j-i]:
            exclude_num += 1

total_ans -= exclude_num

print(total_ans)