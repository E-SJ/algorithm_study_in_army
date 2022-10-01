import sys
sys.setrecursionlimit(10 ** 9)
input=sys.stdin.readline
m,n = map(int,input().split()) #세로,가로
matrix=[]
dp=[[-1 for _ in range(n)] for _ in range(m)]
for _ in range(m):
  matrix.append(list(map(int,input().split())))

dy=[0,1,0,-1]
dx=[1,0,-1,0]
def dfs(y,x):
  global ans
  #print(*dp,sep="\n",end="\n\n")
  if (y==m-1 and x==n-1):
    return 1
  if (dp[y][x]==-1):
    dp[y][x]=0
    for i in range(4):
      ny=y+dy[i]
      nx=x+dx[i]
      if (0<=ny<m and 0<=nx<n and matrix[y][x]>matrix[ny][nx]):
        dp[y][x]+=dfs(ny,nx)
  return dp[y][x]
print(dfs(0,0))
#print(*dp,sep="\n",end="\n\n")


