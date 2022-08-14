""" # DFS 방식
from sys import setrecursionlimit
from sys import stdin
from time import time
setrecursionlimit(10**4)
input=stdin.readline
r,c = map(int,input().split())
board=[]
for _ in range(r):
  board.append(list(map(str,input())))


dxy=[(1,0),(-1,0),(0,1),(0,-1)]
for i in range(r):
  for j in range(c):
    board[i][j] = ord(board[i][j])-65
  del board[i][-1]


def useless_bfs():
  Q=deque()
  visited=[]
  Q.append((0,0))
  visited.append(board[0][0])
  while (len(Q)):
    for _ in range(len(Q)):
      pos = Q.popleft()
      for i in range(4):
        if (0<=pos[0]+dy[i]<r and 0<=pos[1]+dx[i]<c and not board[pos[0]+dy[i]][pos[1]+dx[i]] in visited)


results=set()
visited=[0 for _ in range(26)]

ans = 0
def dfs(y,x,count):
  global ans
  #temp = time.time()
  #printvisited()
  #print(y,x,count,visited)
  for dx,dy in dxy:
    ny,nx=y+dy,x+dx
    if (0<=ny<r and 0<=nx<c and visited[board[ny][nx]]==0):
      alphabet=board[ny][nx]
      visited[alphabet]=1
      dfs(ny,nx,count+1)
      visited[alphabet]=0
      #print(result)
      #print(visited)
  ans=max(count,ans)    
  #print(f"{time.time()-temp:.23f}")

visited[board[0][0]]=1
start=time()
dfs(0,0,1)
print(ans)
#print(time()-start)
"""


""" BFS 방식
from collections import deque
r,c = map(int,input().split())
board=[]
for _ in range(r):
  board.append(list(map(str,input())))

dxy = [(1,0),(-1,0),(0,1),(0,-1)]
ans=0
def bfs(x,y):
  global ans
  Q=set()
  Q.add((x,y,board[y][x]))
  while (len(Q)):
    x,y,z = Q.pop()
    ans=max(ans,len(z))
    for dx,dy in dxy:
      ny,nx=y+dy,x+dx
      if (0<=ny<r and 0<=nx<c and not board[ny][nx] in z):
        if not ((nx,ny,z+board[ny][nx]) in Q):
          Q.add((nx,ny,z+board[ny][nx]))
        
        
bfs(0,0)
print(ans)
"""
# deque로도 구현해보자.

from collections import deque
r,c = map(int,input().split())
board=[]
for _ in range(r):
  board.append(list(map(str,input())))

visited=[['' for _ in range(c)]for _ in range(r)]
dxy = [(1,0),(-1,0),(0,1),(0,-1)]
ans=0

def bfs(x,y):
  global ans
  Q=deque()
  visited[y][x]=board[y][x]
  Q.append((x,y,visited[y][x]))
  while (Q):
    ans+=1
    for _ in range(len(Q)):
      x,y,z = Q.popleft()
      visited[y][x]=''
      for dx,dy in dxy:
        ny,nx=y+dy,x+dx
        if (0<=ny<r and 0<=nx<c and visited[ny][nx]!=z+board[y][x]):
          visited[ny][nx]=z+board[y][x]
          Q.append((nx,ny,visited[y][x]))
          
    print(Q)

bfs(0,0)
print(ans)
