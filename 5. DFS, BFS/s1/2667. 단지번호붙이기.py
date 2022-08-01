n=int(input())
mapp=[]
for _ in range(n):
  mapp.append(list(map(str,input())))
for i in range(n):
  for j in range(n):
    mapp[i][j]=int(mapp[i][j])
def check(y,x,num):
  if (x>0 and mapp[y][x-1]==1):
    mapp[y][x-1]=num
    check(y,x-1,num)
  if (x<n-1 and mapp[y][x+1]==1):
    mapp[y][x+1]=num
    check(y,x+1,num)
  if (y>0 and mapp[y-1][x]==1):
    mapp[y-1][x]=num
    check(y-1,x,num)
  if (y<n-1 and mapp[y+1][x]==1):
    mapp[y+1][x]=num
    check(y+1,x,num)
count=2 #단지 번호 (2부터 시작)
for i in range(n):
  for j in range(n):
    if (mapp[i][j]==1):
      mapp[i][j]=count
      check(i,j,count)
      count+=1
results=[0 for _ in range(count-2)]
for c in range(2,count):
  for i in range(n):
    for j in range(n):
      if (mapp[i][j]==c):
        results[c-2]+=1
results.sort()
print(len(results))
for item in results:
  print(item)
    