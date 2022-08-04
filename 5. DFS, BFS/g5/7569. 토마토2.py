from collections import deque

import copy
m,n,h = map(int,input().split())
tomatoes = []
toripequeue = deque()
ripequeue = deque()
for _ in range(h):
  temp=[]
  for _ in range(n):
    temp.append(list(map(int,input().split())))
  tomatoes.append(temp)

def ripe(z,y,x):
  if (y<n-1 and tomatoes[z][y+1][x]==0):
    tomatoes[z][y+1][x]=1
    toripequeue.append((z,y+1,x))
  if (y>0 and tomatoes[z][y-1][x]==0):
    tomatoes[z][y-1][x]=1
    toripequeue.append((z,y-1,x))
  if (x<m-1 and tomatoes[z][y][x+1]==0):
    tomatoes[z][y][x+1]=1
    toripequeue.append((z,y,x+1))
  if (x>0 and tomatoes[z][y][x-1]==0):
    tomatoes[z][y][x-1]=1
    toripequeue.append((z,y,x-1))
  if (z>0 and tomatoes[z-1][y][x]==0):
    tomatoes[z-1][y][x]=1
    toripequeue.append((z-1,y,x))
  if (z<h-1 and tomatoes[z+1][y][x]==0):
    tomatoes[z+1][y][x]=1
    toripequeue.append((z+1,y,x))
  

count=0

noripeflag=False
for i in range(h):
  for j in range(n):
    if 0 in tomatoes[i][j]:
      noripeflag=True
if (not noripeflag):
  print(0)
  exit()    
for i in range(h):
  for j in range(n):
    for k in range(m):
      if tomatoes[i][j][k]==1:  
        toripequeue.append((i,j,k))

while True:
  count+=1
  ripequeue.extend(list(toripequeue))
  toripequeue.clear()
  for (i,j,k) in ripequeue.copy():
    temp = ripequeue.popleft()
    ripe(temp[0],temp[1],temp[2])
  if (len(toripequeue)==0):
    count-=1
    break

  
for floors in tomatoes:
  for line in floors:
    if 0 in line:
      print(-1)
      exit()
print(count)
        
    
      
