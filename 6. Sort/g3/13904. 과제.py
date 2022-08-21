import sys
input=sys.stdin.readline
n = int(input())
arr=[]
todo=[-1 for _ in range(1001)]
for _ in range(n):
  arr.append(tuple(map(int,input().split())))
arr.sort(key=lambda x:(x[1],-x[0]),reverse=True)

maxd=0
count=0
result=0
for d,w in arr:
  maxd=max(d,maxd)
  if (count<maxd):
    while (todo[d]!=-1 and d>0):
      d-=1
    if (d<=0):
      continue
    result+=w
    todo[d]=w
    count+=1

print(result)
