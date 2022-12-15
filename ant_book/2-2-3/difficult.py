# The range from the first character to the number of characters that can be
# changed in dictionary order is called a "dictionary order change range".
NumStr, ChangeStr = map(int, input().split())
String = list(input())

min_dict_str = sorted(String)

change_cost = 0
check_index = 0
change_index_list = []
if min_dict_str[check_index] != String[check_index]:
    change_index_list.append(check_index)

# Find the index that needs to be changed within 
# the "dictionary order change range".
while change_cost < ChangeStr:
    change_cost = 0

    check_index += 1
    if NumStr <= check_index:
        break
    if min_dict_str[check_index] != String[check_index]:
        change_index_list.append(check_index)

    for i_index, i_dict_str in enumerate(min_dict_str[:check_index+1]):
        if min_dict_str[i_index] == String[i_index]:
            continue

        if i_dict_str in String[:check_index+1]:
            change_cost += 1
        else:
            change_cost += 2

# The index required for the change is obtained from outside
# the "dictionary order change range".
add_candidates = sorted(String[check_index+1:])
add_index = 0
for _ in range(ChangeStr - len(change_index_list)):
    for i_index, i_str in enumerate(String[check_index+1:], check_index+1):
        if i_str == add_candidates[add_index] and \
                                               i_index not in change_index_list:
            change_index_list.append(i_index)
            add_index += 1
            break

# Rearrange the "dictionary order change range".
change_str_list = []
for i_index in change_index_list:
    change_str_list.append(String[i_index])

change_str_list.sort()
for i_index, i_str in zip(change_index_list, change_str_list):
    String[i_index] = i_str

ans = ''.join(String)
print(ans)
exit()