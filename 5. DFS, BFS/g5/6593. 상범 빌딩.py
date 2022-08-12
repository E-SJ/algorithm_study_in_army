from collections import deque

dx=[1,-1,0,0,0,0] # 열
dy=[0,0,1,-1,0,0] # 행
dz=[0,0,0,0,1,-1] # 층

def find_start():
  for i in range(l):
    for j in range(r):
      for k in range(c):
        if (matrix[i][j][k]=='S'):
          return [i,j,k] #층 행 열

def bfs(pos):
  count=1
  visited=[[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
  for i in range(6):
    if ((0<=pos[0]+dz[i]<l and 0<=pos[1]+dy[i]<r and 0<=pos[2]+dx[i]<c) and visited[pos[0]+dz[i]][pos[1]+dy[i]][pos[2]+dx[i]]==0 and matrix[pos[0]+dz[i]][pos[1]+dy[i]][pos[2]+dx[i]]=='.'):
      Q.append([pos[0]+dz[i],pos[1]+dy[i],pos[2]+dx[i]])
      visited[pos[0]+dz[i]][pos[1]+dy[i]][pos[2]+dx[i]]=1
    elif ((0<=pos[0]+dz[i]<l and 0<=pos[1]+dy[i]<r and 0<=pos[2]+dx[i]<c) and visited[pos[0]+dz[i]][pos[1]+dy[i]][pos[2]+dx[i]]==0 and matrix[pos[0]+dz[i]][pos[1]+dy[i]][pos[2]+dx[i]]=='E'):
      return "Escaped in "+str(count)+" minute(s)."
  while(len(Q)):
    count+=1
    for _ in range(len(Q)):
      pos = Q.popleft()
      for i in range(6):
        if ((0<=pos[0]+dz[i]<l and 0<=pos[1]+dy[i]<r and 0<=pos[2]+dx[i]<c) and visited[pos[0]+dz[i]][pos[1]+dy[i]][pos[2]+dx[i]]==0 and matrix[pos[0]+dz[i]][pos[1]+dy[i]][pos[2]+dx[i]]=='.'):
          Q.append([pos[0]+dz[i],pos[1]+dy[i],pos[2]+dx[i]])
          visited[pos[0]+dz[i]][pos[1]+dy[i]][pos[2]+dx[i]]=1
        elif ((0<=pos[0]+dz[i]<l and 0<=pos[1]+dy[i]<r and 0<=pos[2]+dx[i]<c) and visited[pos[0]+dz[i]][pos[1]+dy[i]][pos[2]+dx[i]]==0 and matrix[pos[0]+dz[i]][pos[1]+dy[i]][pos[2]+dx[i]]=='E'):
          return "Escaped in "+str(count)+" minute(s)."
  return "Trapped!"
          
    #print(Q)
    #print(count)
   
while True:
  Q=deque()
  l,r,c = map(int,input().split())
  if (l==0 and r==0 and c==0):
    break
  matrix=[]
  for i in range(l):
    matrix.append([])
    for _ in range(r):
      matrix[i].append(list(map(str,input())))
    input()
  print(bfs(find_start()))
      
  