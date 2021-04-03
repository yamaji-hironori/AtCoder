a, b, c = map(int, input().split())

xflag = False
yflag = False
for i, j in ([a,b],[b,c],[c,a]):
    if i == j:
        xflag = True
    else:
        yflag = True

if xflag and yflag:
    print('Yes')
else:
    print('No')