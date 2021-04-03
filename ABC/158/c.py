import math

A, B = map(int, input().split())

tax_a = 0.08
tax_b = 0.1

start_price = math.ceil(A / tax_a)
stop_price = math.ceil((A+1) / tax_a)

for i_price in range(start_price, stop_price):
    if math.floor(i_price * tax_b) == B:
        ans = i_price
        break
else:
    ans = -1

print(ans)