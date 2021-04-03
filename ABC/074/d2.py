import heapq
n=int(input())
a=[int(i) for i in input().split()]
f=a[:n]
l=[-i for i in a[2*n:]]
heapq.heapify(f)
heapq.heapify(l)
fs=[0]*(n+1)
ls=[0]*(n+1)
fs[0]=sum(f)
ls[n]=-sum(l)

for i in range(n):
    c=a[n+i]
    m=heapq.heappushpop(f,c)
    fs[i+1]=fs[i]+c-m

for i in range(n):
    c=a[2*n-1-i]
    m=heapq.heappushpop(l,-c)
    ls[n-i-1]=ls[n-i]+c+m

ans=fs[0]-ls[0]
for k in range(n+1):
    ans=max(ans,fs[k]-ls[k])
print(ans)
