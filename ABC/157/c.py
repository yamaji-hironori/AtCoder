N, M = map(int, input().split())
S_C_list = [[int(_) for _ in input().split()] for i in range(M)]

ans = 'a' * N

for i_s, i_c in S_C_list:
    if ans[i_s-1] == 'a' or ans[i_s-1] == str(i_c):
        ans = ans[:i_s-1] + str(i_c) + ans[i_s:]
        continue

    ans = '-1'
    break

else:
    if N == 1:
        if ans[0] == 'a':
            ans = '0'

    else:
        if ans[0] == '0':
            ans = '-1'

        elif ans[0] == 'a':
            ans = '1' + ans[1:]

if ans != '-1':
    for i, i_ch in enumerate(ans[1:], 1):
        if i_ch == 'a':
            ans = ans[:i] + '0' + ans[i+1:]

print(int(ans))