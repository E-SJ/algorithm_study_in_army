import copy
m,n = map(int,input().split())
tomatoes = []
for _ in range(n):
  tomatoes.append(list(map(int,input().split())))

def ripe(y,x):
  if (y<n-1 and tomatoes_temp[y+1][x]==0):
    tomatoes_temp[y+1][x]=1
  if (y>0 and tomatoes_temp[y-1][x]==0):
    tomatoes_temp[y-1][x]=1
  if (x<m-1 and tomatoes_temp[y][x+1]==0):
    tomatoes_temp[y][x+1]=1
  if (x>0 and tomatoes_temp[y][x-1]==0):
    tomatoes_temp[y][x-1]=1

count=0

noripeflag=False
for i in range(n):
  if 0 in tomatoes[i]:
    noripeflag=True
if (not noripeflag):
  print(0)
  exit()    



while True:
  count+=1
  ripeflag=True
  noripeflag=False
  tomatoes_temp=copy.deepcopy(tomatoes)
  for i in range(n):
    for j in range(m):
      if tomatoes[i][j]==1:  
        ripe(i,j)

  for i in range(n):
    if 0 in tomatoes[i]:
      noripeflag=True

  if (copy.deepcopy(tomatoes) == copy.deepcopy(tomatoes_temp)):
    ripeflag=False
  tomatoes=copy.deepcopy(tomatoes_temp)


  if (noripeflag and not ripeflag):
    print(-1)
    exit()
  
  if (not noripeflag):
    count-=1
    break
    
print(count)
        
    
      
