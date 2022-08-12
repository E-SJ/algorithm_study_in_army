import copy
import time
from collections import deque
n,m = map(int,input().split())
matrix=[]
for _ in range(n):
  matrix.append(list(map(int,input().split())))
empty=[]
wall=[]
virus=[]
for i in range(n):
  for j in range(m):
    if matrix[i][j]==0:
      empty.append((i,j))
    elif matrix[i][j]==1:
      wall.append((i,j))
    elif matrix[i][j]==2:
      virus.append((i,j))
matrix_ori=copy.deepcopy(matrix)
empty_ori=copy.deepcopy(empty)
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def dfs_virus(pos):
  matrix[pos[0]][pos[1]]=2
  if not ((pos[0],pos[1]) in virus):
    #virus.append((pos[0],pos[1]))
    pass
  for i in range(4):
    if (0<=pos[0]+dy[i]<n and 0<=pos[1]+dx[i]<m and matrix[pos[0]+dy[i]][pos[1]+dx[i]]==0):
      dfs_virus((pos[0]+dy[i],pos[1]+dx[i]))



def bfs_safe(pos):
  Q=deque()
  visit=[[0 for _ in range(m)] for _ in range(n)]
  visit[pos[0]][pos[1]]=1
  for i in range(4):
    if (0<=pos[0]+dy[i]<n and 0<=pos[1]+dx[i]<m and matrix[pos[0]+dy[i]][pos[1]+dx[i]]==0 and visit[pos[0]+dy[i]][pos[1]+dx[i]]==0):
      Q.append((pos[0]+dy[i],pos[1]+dx[i]))
      visit[pos[0]+dy[i]][pos[1]+dx[i]]=1
  while len(Q):
    for _ in range(len(Q)):
      pos = Q.popleft()
      for i in range(4):
        if (0<=pos[0]+dy[i]<n and 0<=pos[1]+dx[i]<m and matrix[pos[0]+dy[i]][pos[1]+dx[i]]==0 and visit[pos[0]+dy[i]][pos[1]+dx[i]]==0):
          Q.append((pos[0]+dy[i],pos[1]+dx[i]))
          visit[pos[0]+dy[i]][pos[1]+dx[i]]=1
  return len(visit)
      
  
#for y,x in virus:
#  dfs_virus((y,x))
print (empty)
results=[]
for i in range(len(empty)-2):
  for j in range(i+1,len(empty)-1):
    for k in range(j+1,len(empty)):
      matrix[empty[i][0]][empty[i][1]]=1
      matrix[empty[j][0]][empty[j][1]]=1
      matrix[empty[k][0]][empty[k][1]]=1
      empty.extend([(empty[k][0],empty[k][1]),(empty[j][0],empty[j][1]),(empty[k][0],empty[k][1])])
      
      for y,x in virus:
        dfs_virus((y,x))
      for y,x in empty:
        results.append(bfs_safe((y,x)))
        print(results[-1])
      print(matrix)
      time.sleep(2)
      empty=empty_ori
      matrix=matrix_ori
print(max(results))

      