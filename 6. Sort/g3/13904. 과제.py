import sys
input=sys.stdin.readline
n = int(input())
arr=[]
for _ in range(n):
  arr.append(tuple(map(int,input().split())))
arr.sort(key=lambda x:(-x[0],-x[1]))
#print(arr)
todo=[0 for _ in range(arr[0][0]+1)]
for day in range(arr[0][0],0,-1):
  max=0
  maxindex=-1
  for i in range(len(arr)):
    #print(arr)
    if (arr[i][0]>=day):
      if (arr[i][1]>max):
        max = arr[i][1]
        maxindex=i
    else:
      break
  todo[day]=max
  if (maxindex!=-1):
    arr.pop(maxindex)

#print(todo)
print(sum(todo))
  


""" 구 코드
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
"""