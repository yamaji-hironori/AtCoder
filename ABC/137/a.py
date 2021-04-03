A, B = map(int, input().split())

add = A + B
dec = A - B
rid = A * B

print(max(add, dec, rid))