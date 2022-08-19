import sys
input=sys.stdin.readline
n= int(input())
arr=[]
check=[0 for _ in range(n)]
for _ in range(n):
  arr.append(int(input()))

arr.sort(reverse=True)
result=0
point=0
#print(arr)
while True:
  if point+1>=n or arr[point]<=0:
    break
  if (arr[point]>1 and arr[point+1]>1):
    result+=(arr[point]*arr[point+1])
    check[point]=1
    check[point+1]=1
    #print("add",(arr[point1]*arr[point1+1]))
    point+=2
  else:
    point+=1

point=n-1
while True:
  if point-1<0 or arr[point-1]>0:
    break
  if (arr[point]<=-1 and arr[point-1]<=0):
    result+=(arr[point]*arr[point-1])
    check[point]=1
    check[point-1]=1
    #print("add",(arr[point1]*arr[point1+1]))
    point-=2
  else:
    point-=1
    
for i in range(n):
  if (check[i]==0):
    result+=arr[i]
print(result)