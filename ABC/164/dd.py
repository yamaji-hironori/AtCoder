S = input()
s_reverse = S[::-1]

dp = [0]*2019
now_sum = 0
ten_times = 1

for ch in s_reverse:
    now_sum = (now_sum + int(ch)*ten_times) % 2019
    ten_times = (ten_times * 10) % 2019
    dp[now_sum] += 1

ans = dp[0]
for i_dp in dp:
    ans += i_dp*(i_dp-1)//2

print(ans)