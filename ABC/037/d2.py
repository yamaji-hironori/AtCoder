import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def main():
  MOD = 10**9+7
  h, w = map(int, input().split())
  M = h*w
  A = [list(map(int, input().split())) for _ in range(h)]

  dp = [-1]*M
  def dfs(v):
    if dp[v] != -1:
      return dp[v]
    i, j = divmod(v, w)
    count = 1
    for dy, dx in ((-1, 0), (0, -1), (1, 0), (0, 1)):
      y, x = i+dy, j+dx
      if 0 <= y < h and 0 <= x < w:
        if A[i][j] < A[y][x]:
          count += dfs(w*y+x)
    count %= MOD
    dp[v] = count
    return count

  ans = 0
  for i in range(M):
    ans += dfs(i)
    ans %= MOD
  print(ans)

if __name__ == "__main__":
  main()
