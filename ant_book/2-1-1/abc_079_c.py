abcd = input()

abcd_list = []

def plus_or_minas(abcd_str, pos, abcd):
    if pos == 4:
        abcd_list.append(abcd_str)
        return

    plus_or_minas(abcd_str+'+'+abcd[pos], pos+1, abcd)
    plus_or_minas(abcd_str+'-'+abcd[pos], pos+1, abcd)
    return

plus_or_minas(abcd[0], 1, abcd)

for i_abcd in abcd_list:
    if eval(i_abcd) == 7:
        print(i_abcd+'=7')
        exit()