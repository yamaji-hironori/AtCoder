n, y = map(int, input().split())

for i in range(n+1):
    for j in range(n-i+1):
        price = 10000*i + 5000*j + 1000*(n-i-j)
        if price == y:
            print(i, j, (n-i-j))
            exit()
        
print(-1, -1, -1)