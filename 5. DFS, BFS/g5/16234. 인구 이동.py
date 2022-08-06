import sys
sys.setrecursionlimit(10**5)
n,l,r = map(int,input().split())
A=[]
for _ in range(n):
  A.append(list(map(int,input().split())))

def open(y,x):
  openflag=False
  if (y>0 and A_group[y-1][x]==0 and (abs(A[y][x]-A[y-1][x])>=l and abs(A[y][x]-A[y-1][x])<=r)):
    A_group[y][x]=groupnum
    A_group[y-1][x]=groupnum
    if not ((y,x) in tomovecountry):
      tomovecountry.append((y,x))
    tomovecountry.append((y-1,x))
    openflag=True
    open(y-1,x)
  if (y<n-1 and A_group[y+1][x]==0 and (abs(A[y][x]-A[y+1][x])>=l and abs(A[y][x]-A[y+1][x])<=r)):
    A_group[y][x]=groupnum
    A_group[y+1][x]=groupnum
    if not ((y,x) in tomovecountry):
      tomovecountry.append((y,x))
    tomovecountry.append((y+1,x))
    openflag=True
    open(y+1,x)
  if (x>0 and A_group[y][x-1]==0 and (abs(A[y][x]-A[y][x-1])>=l and abs(A[y][x]-A[y][x-1])<=r)):
    A_group[y][x]=groupnum
    A_group[y][x-1]=groupnum
    if not ((y,x) in tomovecountry):
      tomovecountry.append((y,x))
    tomovecountry.append((y,x-1))
    openflag=True
    open(y,x-1)
  if (x<n-1 and A_group[y][x+1]==0 and (abs(A[y][x]-A[y][x+1])>=l and abs(A[y][x]-A[y][x+1])<=r)):
    A_group[y][x]=groupnum
    A_group[y][x+1]=groupnum
    if not ((y,x) in tomovecountry):
      tomovecountry.append((y,x))
    tomovecountry.append((y,x+1))
    openflag=True
    open(y,x+1)
  return openflag

day = 0
movedcountry=[]
while True:
  tomovecountry=[]
  groupnum=1
  sum_pop=[[0,0]]
  A_group=[[0 for _ in range(n)] for _ in range(n)]
  for y in range(n):
    for x in range(n):
      
      if (A_group[y][x]==0):
        if (open(y,x)):
          groupnum+=1
      if (A_group[y][x]!=0):
        while (len(sum_pop)<=A_group[y][x]):
          sum_pop.append([0,0])
        sum_pop[A_group[y][x]][0]+=A[y][x]
        sum_pop[A_group[y][x]][1]+=1
  if (groupnum==1): #인구이동 없으면
    break
  day+=1
  
  # 각 index가 그룹 넘버가 되고, 그 값의 첫번째 인덱스는 그 그룹의 총 인구, 두번째 인덱스는 그 그룹의 총 나라의 수이다.
      
  countries = 0
  for item in sum_pop:
    countries+=item[1]
  for y,x in tomovecountry:
      groupnum = A_group[y][x]
      if (groupnum!=0):
        A[y][x]=int(sum_pop[groupnum][0]/sum_pop[groupnum][1])
  movedcountry.extend(tomovecountry)

print(day)
