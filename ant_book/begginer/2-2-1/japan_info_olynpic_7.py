price = int(input())

change = 1000 - price
ans = 0

for coin in (500, 100, 50, 10, 5, 1):
    ans += change // coin
    change = change % coin

print(ans)