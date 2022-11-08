import sys
import copy
from collections import deque
input=sys.stdin.readline
n,m = map(int,input().split())
matrix=[]
for _ in range(n):
  matrix.append(list(map(int,input().rstrip())))
dp=copy.deepcopy(matrix)
for y in range(n):
  for x in range(m):
    if dp[y][x]==1:
      dp[y][x]=-1

dydx=[(0,1),(0,-1),(1,0),(-1,0)]

adjnodesnums=copy.deepcopy(dp)

visited=copy.deepcopy(matrix)
adjnodesnum=0
#print(*visited,sep='\n')
for i in range(n):
  for j in range(m):
    #print(i,j,dp[i][j],visited[i][j])
    if (dp[i][j]==0 and visited[i][j]==0):
      #print("CURRENT",i,j)
      adjnodesnum+=1
      adjnodes=[(i,j)]
      visited[i][j]=1
      q=deque()
      q.append((i,j))
      while q:
        y,x = q.popleft()
        for dy,dx in dydx:
          ny,nx=y+dy,x+dx
          if (0<=ny<n and 0<=nx<m and visited[ny][nx]==0):
            visited[ny][nx]=1
            adjnodes.append((ny,nx))
            q.append((ny,nx))
      for y,x in adjnodes:
        dp[y][x]=len(adjnodes)
        adjnodesnums[y][x]=adjnodesnum

for y in range(n):
  for x in range(m):
    if (matrix[y][x]==1):
      AddedAdjnodenums=[]
      for dy,dx in dydx:
        ny,nx=y+dy,x+dx
        if (0<=ny<n and 0<=nx<m and adjnodesnums[ny][nx] not in AddedAdjnodenums and adjnodesnums[ny][nx]!=-1):
          matrix[y][x]+=dp[ny][nx]
          AddedAdjnodenums.append(adjnodesnums[ny][nx])
          
for y in range(n):
  for x in range(m):
    matrix[y][x]%=10
              
#print(*dp,sep='\n')
for line in matrix:
  print(*line,sep='')
#print(*adjnodesnums,sep='\n')