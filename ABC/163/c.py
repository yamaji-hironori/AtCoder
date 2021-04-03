N = int(input())
A = list(map(int, input().split()))

b = [0]*N
for i_a in A:
    b[i_a-1] += 1

for i_b in b:
    print(i_b)