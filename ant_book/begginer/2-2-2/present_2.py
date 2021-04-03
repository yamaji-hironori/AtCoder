#LIS_にぶたん解法

import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    
    
    N=I()
    wh=[[0,0]for _ in range(N)]
    for i in range(N):
        wh[i][0],wh[i][1]=MI()
    #wが昇順，hが降順になるように並べたのちに，hが昇順になるように取り出せば必ずwも昇順になる．
    wh.sort(key=lambda x:(x[0],-x[1]))
    
    inf=10**6
    #dp[i]は，長さiの増加部分列を作るときの，最後の番号の最小値
    dp=[inf]*N
    import bisect
    ans=0
    
    for i in range(N):
        h=wh[i][1]
        a=bisect.bisect_left(dp,h)
        dp[a]=h
        ans=max(ans,a)
        
    print(ans+1)

main()