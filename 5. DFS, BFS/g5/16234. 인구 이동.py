n,l,r = map(int,input().split())
A=[]
for _ in range(n):
  A.append(list(map(int,input().split())))
A_group=[[0 for _ in range(n)] for _ in range(n)]
def open(y,x):
  if (y>0 and A_group[y-1][x]==0 and (abs(A[y][x]-A[y-1][x])>=l and abs(A[y][x]-A[y-1][x])<=r)):
    A_group[y][x]=groupnum
    A_group[y-1][x]=groupnum
    open(y-1,x)
  if (y<n-1 and A_group[y+1][x]==0 and (abs(A[y][x]-A[y+1][x])>=l and abs(A[y][x]-A[y+1][x])<=r)):
    A_group[y][x]=groupnum
    A_group[y+1][x]=groupnum
    open(y+1,x)
  if (x>0 and A_group[y][x-1]==0 and (abs(A[y][x]-A[y][x-1])>=l and abs(A[y][x]-A[y][x-1])<=r)):
    A_group[y][x]=groupnum
    A_group[y][x-1]=groupnum
    open(y,x-1)
  if (x<n-1 and A_group[y][x+1]==0 and (abs(A[y][x]-A[y][x+1])>=l and abs(A[y][x]-A[y][x+1])<=r)):
    A_group[y][x]=groupnum
    A_group[y][x+1]=groupnum
    open(y,x+1)
  
groupnum=1
for y in range(n):
  for x in range(n):
    if (A_group[y][x]==0):
      open(y,x)
      groupnum+=1
print(A_group)


### 이 아래부터 어렵다~
def cal(y,x,num):
  A_group[y][x]=-1
  results=[]
  if (y>0 and A_group[y-1][x]==num):
    result = cal(y-1,x,num)+1
    results.append(result)
  if (y<n-1 and A_group[y+1][x]==num):
    result = cal(y+1,x,num)+1
    results.append(result)
  if (x>0 and A_group[y][x-1]==num):
    result = cal(y,x-1,num)+1
    results.append(result)
  if (x<n-1 and A_group[y][x+1]==num):
    result = cal(y,x+1,num)+1
    results.append(result)
  if len(results)==0:
    return 0
  else:
    return max(results)

for y in range(n):
  for x in range(n):
    if (A_group[y][x]!=0 and A_group[y][x]!=-1):
      result = cal(y,x,A_group[y][x])
print(result)
      