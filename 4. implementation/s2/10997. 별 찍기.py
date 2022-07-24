n=int(input())
if (n==1):
  print("*")
else:
  mapp=[]
  row=-1+4*n
  col=-3+4*n
  for y in range(row):
    mapp.append([" " for _ in range(col)])
  
  pos=[row-1,0]
  for i in range(row):
    mapp[i][0]="*"
  for i in range(col):
    mapp[0][i]="*"
  
  iter=row-3
  for _ in range(n-1):
    for i in range(iter):
      pos[1]+=1
      mapp[pos[0]][pos[1]]="*"
    for i in range(iter):
      pos[0]-=1
      mapp[pos[0]][pos[1]]="*"
    iter-=2
    for i in range(iter):
      pos[1]-=1
      mapp[pos[0]][pos[1]]="*"
    for i in range(iter):
      pos[0]+=1
      mapp[pos[0]][pos[1]]="*"
    iter-=2
  for i in range(row):
    if (i==1):
      print('*',end="\n")
      continue
    for j in range(col):
      print(mapp[i][j],end="")
    if (i<row-1):
      print()