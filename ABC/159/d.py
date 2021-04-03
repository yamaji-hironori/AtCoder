N = int(input())
A_list = list(map(int, input().split()))

dp = [0] * (N+1)

for i_A in A_list:
    dp[i_A] += 1

total = 0
for i_dp in dp:
    total += (i_dp*(i_dp-1)) // 2

for i_A in A_list:
    diff = (dp[i_A]*(dp[i_A]-1))//2 - ((dp[i_A]-1)*(dp[i_A]-2))//2
    print(total - diff)