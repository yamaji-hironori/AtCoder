S = input()
S_reverse = S[::-1]

dp = [0] * 2019
now_mod = 0
digit = 1

for i_s in S_reverse:
    now_mod = (now_mod + int(i_s)*digit) % 2019
    digit = (digit*10) % 2019
    dp[now_mod] += 1

ans = sum(x*(x-1)//2 for x in dp)
ans += dp[0]

print(ans)