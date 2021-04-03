a, b, c = list(map(int, input().split()))

a, b = b, a
a, c = c, a

print(a,b,c)