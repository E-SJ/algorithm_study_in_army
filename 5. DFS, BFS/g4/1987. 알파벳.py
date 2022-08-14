import sys
from collections import deque
import time
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
r,c = map(int,input().split())
board=[]
for _ in range(r):
  board.append(list(map(str,input())))
dx=[0,1,0,-1]
dy=[1,0,-1,0]
for i in range(r):
  for j in range(c):
    board[i][j] = ord(board[i][j])-65
  del board[i][-1]

"""
def bfs():
  Q=deque()
  visited=[]
  Q.append((0,0))
  visited.append(board[0][0])
  while (len(Q)):
    for _ in range(len(Q)):
      pos = Q.popleft()
      for i in range(4):
        if (0<=pos[0]+dy[i]<r and 0<=pos[1]+dx[i]<c and not board[pos[0]+dy[i]][pos[1]+dx[i]] in visited)
"""

results=set()
visited=[0 for _ in range(26)]

ans = 0
def dfs(y,x,count):
  global ans
  #temp = time.time()
  #printvisited()
  #print(y,x,count,visited)
  for i in range(4):
    ny,nx=y+dy[i],x+dx[i]
    if (0<=ny<r and 0<=nx<c and visited[board[y+dy[i]][x+dx[i]]]==0):
      alphabet=board[ny][nx]
      visited[alphabet]=1
      dfs(ny,nx,count+1)
      visited[alphabet]=0
      #print(result)
      #print(visited)
  ans=max(count,ans)    
  #print(f"{time.time()-temp:.23f}")

visited[board[0][0]]=1
dfs(0,0,1)
print(ans)

  