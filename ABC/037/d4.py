import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)
mod=10**9+7

H,W=map(int,input().split())
L=[]
l=[-1 for i in range(W+2)]
L.append(l)

for i in range(H):
    a=[-1]+list(map(int,input().split()))+[-1]
    L.append(a)
L.append(l)

A=[]
a=[0 for i in range(W+2)]
A.append(a)
for i in range(H):
    b=[0]+[-1 for j in range(W)]+[0]
    A.append(b)
A.append(a)

#print(L)
#print(A)

def count(h,w):
    cnt=1
    if A[h][w]!=-1:
        return A[h][w]
    else:
        if L[h+1][w]>L[h][w]:
            cnt+=count(h+1,w)
        if L[h-1][w]>L[h][w]:
            cnt+=count(h-1,w)
        if L[h][w+1]>L[h][w]:
            cnt+=count(h,w+1)
        if L[h][w-1]>L[h][w]:
            cnt+=count(h,w-1)
        A[h][w]=(cnt%mod)
        return cnt%mod
ans=0
for h in range(1,H+1):
    for w in range(1,W+1):
        if A[h][w]==-1:
            count(h,w)
        ans+=A[h][w]
#print(A)
print(ans%mod)
