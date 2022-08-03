from collections import deque

import copy
m,n = map(int,input().split())
tomatoes = []
toripequeue = deque()
ripequeue = deque()
for _ in range(n):
  tomatoes.append(list(map(int,input().split())))

def ripe(y,x):
  if (y<n-1 and tomatoes[y+1][x]==0):
    tomatoes[y+1][x]=1
    toripequeue.append((y+1,x))
  if (y>0 and tomatoes[y-1][x]==0):
    tomatoes[y-1][x]=1
    toripequeue.append((y-1,x))
  if (x<m-1 and tomatoes[y][x+1]==0):
    tomatoes[y][x+1]=1
    toripequeue.append((y,x+1))
  if (x>0 and tomatoes[y][x-1]==0):
    tomatoes[y][x-1]=1
    toripequeue.append((y,x-1))
  

count=0

noripeflag=False
for i in range(n):
  if 0 in tomatoes[i]:
    noripeflag=True
if (not noripeflag):
  print(0)
  exit()    

for i in range(n):
    for j in range(m):
      if tomatoes[i][j]==1:  
        toripequeue.append((i,j))

while True:
  count+=1
  ripequeue.extend(list(toripequeue))
  toripequeue.clear()
  for (i,j) in ripequeue.copy():
    temp = ripequeue.popleft()
    ripe(temp[0],temp[1])
  if (len(toripequeue)==0):
    count-=1
    break

  
for line in tomatoes:
  if 0 in line:
    print(-1)
    exit()
print(count)
        
    
      
