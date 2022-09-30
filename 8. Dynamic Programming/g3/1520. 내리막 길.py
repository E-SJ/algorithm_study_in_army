import sys
input=sys.stdin.readline
m,n = map(int,input().split()) #세로,가로
matrix=[]
dp=[[-1 for _ in range(n)] for _ in range(m)]
for _ in range(m):
  matrix.append(list(map(int,input().split())))
dp[0][0]=1

def dfs(y,x):
  print(*dp,sep="\n",end="\n\n")
  if (y==m-1 and x==n-1):
    return 1
  if (y+1<m and matrix[y][x]>matrix[y+1][x]):
    if (dp[y+1][x]==-1):
      dp[y+1][x]=dp[y][x]
      dp[y+1][x]+=dfs(y+1,x)
    else:
      dp[y+1][x]=max(dp[y][x]+dfs(y+1,x),dp[y+1][x])
  if (x+1<n and matrix[y][x]>matrix[y][x+1]):
    if (dp[y][x+1]==-1):
      dp[y][x+1]=dp[y][x]
      dp[y][x+1]+=dfs(y,x+1)
    else:
      dp[y][x+1]=max(dp[y][x]+dfs(y,x+1),dp[y][x+1])
  if (0<=y-1 and matrix[y][x]>matrix[y-1][x]):
    if (dp[y-1][x]==-1):
      dp[y-1][x]=dp[y][x]
      dp[y-1][x]+=dfs(y-1,x)
    else:
      dp[y-1][x]=max(dp[y][x]+dfs(y-1,x),dp[y-1][x])
  if (0<=x-1 and matrix[y][x]>matrix[y][x-1]):
    if (dp[y][x-1]==-1):
      dp[y][x-1]=dp[y][x]
      dp[y][x-1]+=dfs(y,x-1)
    else:
      dp[y][x-1]=max(dp[y][x]+dfs(y,x-1),dp[y][x-1])
  return dp[y][x]
dfs(0,0)
print(*dp,sep="\n",end="\n\n")
print(dp[m-1][n-1])

