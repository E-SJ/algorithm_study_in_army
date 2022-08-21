import sys
input=sys.stdin.readline
n = int(input())
if (n==0):
  print(0)
  exit()
arr=[]
for _ in range(n):
  p,d = map(int,input().split())
  arr.append((d,p))
arr.sort(key=lambda x:(-x[0],-x[1]))
#print(arr)
#todo=[0 for _ in range(arr[0][0]+1)]
result=0
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
  #todo[day]=max
  result+=max
  if (maxindex!=-1):
    arr.pop(maxindex)

#print(todo)
print(result)