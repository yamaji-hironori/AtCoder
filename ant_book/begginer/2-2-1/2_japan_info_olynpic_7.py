Price = int(input())
change = 1000 - Price

num_coins = 0
for coin in (500, 100, 50, 10, 5, 1):
    num_coins += change // coin
    change %= coin

print(num_coins) 