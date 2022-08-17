from sys import stdin
from collections import deque
input=stdin.readline
n,m = map(int,input().split())
dyx=[(0,1),(0,-1),(1,0),(-1,0)]
matrix=[]
for _ in range(n):
  matrix.append(list(map(int,input().rstrip())))
visited=[[0 for _ in range(m)] for _ in range(n)]

def bfs(y,x):
  q=deque()
  q.append([y,x,False])
  count=1
  while q:
    for _ in range(len(q)):
      y,x,flag=q.popleft()
      if (y==n-1 and x==m-1):
        print(count)
        exit()
      for dy,dx in dyx:
        ny,nx=y+dy,x+dx
        if (0<=ny<n and 0<=nx<m and visited[ny][nx]!=1):
          if (flag==False and matrix[ny][nx]==1 and visited[ny][nx]!=2):
            visited[ny][nx]=2
            q.append([ny,nx,True])
          elif (flag==False and matrix[ny][nx]==0):
            visited[ny][nx]=1
            q.append([ny,nx,False])
          elif (flag==True and matrix[ny][nx]==0):
            visited[ny][nx]=1
            q.append([ny,nx,True])
          
            
    count+=1

bfs(0,0)
print(-1)