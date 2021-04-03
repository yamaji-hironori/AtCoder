def add_or_do_nothing(s, i, pos):
    if i == len(s):
        pre_i = 0
        ans = 0
        for i, pos_i in enumerate(pos, 1):
            if pos_i == '1':
                ans += int(s[pre_i:i])
                pre_i = i

        ans += int(s[pre_i:len(s)])
        return ans

    f_ans = add_or_do_nothing(s, i+1, pos+'0')
    s_ans = add_or_do_nothing(s, i+1, pos+'1')
    return f_ans + s_ans

s = input()

pos = ''
ans = add_or_do_nothing(s, 1, pos)

print(ans)
