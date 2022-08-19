import sys
input=sys.stdin.readline
n,m = map(int,input().split())
arr=[]
for _ in range(n):
  arr.append(int(input()))
arr.sort()

if n==1:
  print(0)
  exit()
elif n>1:
  point1=0
  point2=1
  ans=2000000001
  while True:
    if (point2>=n):
      break
    temp=arr[point2]-arr[point1]
    if temp<m:
      point2+=1
    elif temp>m:
      point1+=1
      ans=min(ans,temp)
    else:
      print(temp)
      exit()
  print(ans)

