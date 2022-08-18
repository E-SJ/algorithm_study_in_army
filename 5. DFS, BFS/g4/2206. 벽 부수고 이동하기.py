from sys import stdin
from collections import deque
input=stdin.readline
n,m = map(int,input().split())
dyx=[(0,1),(0,-1),(1,0),(-1,0)]
matrix=[]
for _ in range(n):
  matrix.append(list(map(int,input().rstrip())))
visited_1=[[0 for _ in range(m)] for _ in range(n)]
visited_2=[[0 for _ in range(m)] for _ in range(n)]

def bfs(y,x):
  q=deque()
  q.append((y,x,False))
  visited_1[y][x]=1
  visited_2[y][x]=1
  count=1
  while q:
    for _ in range(len(q)):
      y,x,flag=q.popleft()
      if (y==n-1 and x==m-1):
        print(count)
        exit()
      for dy,dx in dyx:
        ny,nx=y+dy,x+dx
        if (0<=ny<n and 0<=nx<m):
          if (flag==False and matrix[ny][nx]==1 and visited_2[ny][nx]!=1):
            visited_2[ny][nx]=1
            q.append((ny,nx,True))
          elif (flag==False and matrix[ny][nx]==0 and visited_1[ny][nx]!=1):
            visited_1[ny][nx]=1
            q.append((ny,nx,False))
          elif (flag==True and matrix[ny][nx]==0 and visited_2[ny][nx]!=1):
            visited_2[ny][nx]=1
            q.append((ny,nx,True))
          
    #print(q)
    count+=1

bfs(0,0)
print(-1)