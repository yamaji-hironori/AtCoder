KeyString = input()
PartString = input()

ans_string = 'UNRESTORABLE'
for i_key in range(len(KeyString)-1,len(KeyString)-len(PartString)-1,-1):
    i_adjust = 0
    for i_part in range(len(PartString)-1, -1, -1):
        if KeyString[i_key-i_adjust] != PartString[i_part] and \
                                               KeyString[i_key-i_adjust] != '?':
            break
        i_adjust += 1

    else:
        ans_string = KeyString[:i_key-len(PartString)+1] + PartString + \
                                                             KeyString[i_key+1:]
        ans_string = ans_string.replace('?', 'a')
        break

print(ans_string)