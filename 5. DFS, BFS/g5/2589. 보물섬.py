from collections import deque

def bfs(y,x):
  visited=[[0 for _ in range(col)] for _ in range(row)]
  Q.append((y,x))
  visited[y][x]=1
  length=-1
  while (len(Q)):
    for _ in range(len(Q)):
      y,x = Q.popleft()
      for k in range(4):
        if (0<=y+dy[k]<row and 0<=x+dx[k]<col and matrix[y+dy[k]][x+dx[k]]=='L' and visited[y+dy[k]][x+dx[k]] == 0):
          visited[y+dy[k]][x+dx[k]]=1
          Q.append((y+dy[k],x+dx[k]))
    length+=1
    print(Q)
  
  return length


def dfs(y,x,num):
  matrix[y][x]=num
  lands[num].append((y,x))
  for k in range(4):
    if (0<=y+dy[k]<row and 0<=x+dx[k]<col and matrix[y+dy[k]][x+dx[k]]=='L'):
      dfs(y+dy[k],x+dx[k],num)
    


Q=deque()
row,col = map(int,input().split())
matrix=[]
for _ in range(row):
  matrix.append(list(map(str,input())))
dx=[1,0,-1,0]
dy=[0,1,0,-1]
landnum=1
lands=[0]
"""
for y in range(row):
  for x in range(col):
    if matrix[y][x]=='L':
      lands.append([])
      dfs(y,x,landnum)
      landnum+=1
"""
times=[]
"""
for num in range(1,landnum):
  for y,x in lands[num]:
    times.append(bfs(y,x,num))
"""

for y in range(row):
  for x in range(col):
    if matrix[y][x]=='L':
      times.append(bfs(y,x))
print(max(times))