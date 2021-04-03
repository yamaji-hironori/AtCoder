from collections import deque

KeyString = input()
PartKeyString = input()

ans_string = 'UNRESTORABLE'
for i_part_pos, i_part_letter in enumerate(PartKeyString):
    if not i_part_letter in KeyString:
        continue

    letter_position_que = deque()
    for j_pos, j_letter in enumerate(KeyString):
        if j_letter == i_part_letter and 0 <= j_pos-i_part_pos and \
                      j_pos + len(PartKeyString) - i_part_pos <= len(KeyString):
            letter_position_que.append(j_pos)

    while len(letter_position_que) > 0:
        letter_position = letter_position_que.pop()

        start_letter_pos = letter_position - i_part_pos
        for k_part_pos, letter in enumerate( \
               KeyString[start_letter_pos:start_letter_pos+len(PartKeyString)]):
            if letter != PartKeyString[k_part_pos] and letter != '?':
                break

        else:
            ans_string = KeyString[:start_letter_pos] + PartKeyString + \
                                 KeyString[start_letter_pos+len(PartKeyString):]
            ans_string = ans_string.replace('?', 'a')
            break

    if ans_string != 'UNRESTORABLE':
        break

else:
    question_num = 0
    start_pos = len(KeyString) - len(PartKeyString)
    for i_pos, i_letter in enumerate(KeyString[::-1]):
        i_pos = len(KeyString) - i_pos - 1
        if i_letter != '?':
            question_num = 0
            start_pos = i_pos - len(PartKeyString)
            continue

        question_num += 1
        if question_num == len(PartKeyString):
            ans_string = KeyString[:start_pos] + PartKeyString + \
                                        KeyString[start_pos+len(PartKeyString):]
            ans_string = ans_string.replace('?', 'a')

print(ans_string)
exit()
