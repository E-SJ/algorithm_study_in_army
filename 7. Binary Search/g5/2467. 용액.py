#이분 탐색 O(NlogN)
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
#print(arr)
ans=2000000001
ans_tuple=tuple()
for i in range(n-1):
  left=i+1
  right=n-1
  while left<=right:
    mid=(left+right)//2
    if (abs(arr[i]+arr[mid])<ans):
      ans=abs(arr[i]+arr[mid])
      ans_tuple=(arr[i],arr[mid])
    if arr[i]+arr[mid]>0:
      right=mid-1
    elif arr[i]+arr[mid]<0:
      left=mid+1
    else:
      print(arr[i],arr[mid])
      exit()
  
    
print(*ans_tuple)

""" 투포인터 O(N)
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
ans=2000000001
ans_tuple=tuple()
p1=0
p2=n-1
while p1<p2:
  value=arr[p1]+arr[p2]
  if (ans>abs(value)):
    ans=abs(value)
    ans_tuple=(arr[p1],arr[p2])
  if value<0:
    p1+=1
  elif value>0:
    p2-=1
  else:
    print(arr[p1],arr[p2])
    exit()
print(*ans_tuple)
"""