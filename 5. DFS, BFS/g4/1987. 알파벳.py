from sys import setrecursionlimit
setrecursionlimit(10**6)
r,c = map(int,input().split())
board=[]
for _ in range(r):
  board.append(list(map(str,input())))
dx=[0,1,0,-1]
dy=[1,0,-1,0]
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
def dfs(y,x,visited):
  #print(y,x,count,visited)
  alphabet=ord(board[y][x])
  if (visited[alphabet-65]==0):
    visited[alphabet-65]=1
  else:
    return
  for i in range(4):
    if (0<=y+dy[i]<r and 0<=x+dx[i]<c):
      dfs(y+dy[i],x+dx[i],visited[:])
    else:
      result=0
      for item in visited:
        if (item==1):
          result+=1
      results.add(result)
      #print(result)

dfs(0,0,[0 for _ in range(26)])
print(max(results))

  