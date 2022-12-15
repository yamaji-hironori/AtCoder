s = input()

math_str_list = []

def plus_or_nothing(math_str, pos_str, s):
    if pos_str == len(s):
        math_str_list.append(eval(math_str))
        return
    
    plus_or_nothing(math_str+s[pos_str], pos_str+1, s)
    plus_or_nothing(math_str+'+'+s[pos_str], pos_str+1, s)
    return

plus_or_nothing(s[0], 1, s)

ans = 0
for i in math_str_list:
    ans += i

print(ans)