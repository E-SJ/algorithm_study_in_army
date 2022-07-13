n,m = map(int,input().split())
mapp=[]
checkflag=[]
for i in range(n):
  mapp.append(list(map(int,input())))
  checkflag.append([0 for _ in range(m)])

def check (y,x):
  if (checkflag[y][x]==1 or mapp[y][x]==1):
    return 0
  else:
    checkflag[y][x]=1
    if (y>=1):
      check(y-1,x)
    if y<n-1:
      check(y+1,x)
    if x>=1:
      check(y,x-1)
    if x<m-1:
      check(y,x+1)
    return 1

result=0
for i in range(n):
  for j in range(m):
    result+=check(i,j)

print(result)