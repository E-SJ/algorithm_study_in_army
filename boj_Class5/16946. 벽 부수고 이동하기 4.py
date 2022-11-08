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
for y in range(n):
  for x in range(m):
    if (dp[y][x]==0 and visited[y][x]==0):
      adjnodesnum+=1
      adjnodes=[(y,x)]
      visited[y][x]=1
      q=deque()
      q.append((y,x))
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
        if (0<=ny<n and 0<=nx<m and matrix[ny][nx]==0 and not adjnodesnums[ny][nx] in AddedAdjnodenums):
          matrix[y][x]+=dp[ny][nx]
          AddedAdjnodenums.append(adjnodesnums[ny][nx])
          
for y in range(n):
  for x in range(m):
    matrix[y][x]%=10
              
#print(*dp,sep='\n')
for line in matrix:
  print(*line,sep='')
#print(*matrix,sep='\n')
#print(*adjnodesnums,sep='\n')