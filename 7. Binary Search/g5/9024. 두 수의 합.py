import sys
from bisect import bisect_left, bisect_right
input=sys.stdin.readline
t = int(input())
for T in range(t):
  n,k = map(int,input().split())
  arr = list(map(int,input().split()))
  arr.sort()
  count=0
  min_distance=10**9
  for i in range(n):
    target=k-arr[i]
    v1=arr[i]
    left=i+1
    right=n-1
    while left<=right:
      mid=(left+right)//2
      v2=arr[mid]
      if (abs(target-arr[mid])==min_distance):
        count+=1
      elif (abs(target-arr[mid])<min_distance):
        min_distance=abs(target-arr[mid])
        count=1
      if arr[mid]>target:
        right=mid-1
      elif arr[mid]<target:
        left=mid+1
      else:
        break
  ans=0
  #for i in range(n):
    #ans+=bisect_right(arr[i+1:],k-arr[i]-min_distance)-bisect_left(arr[i+1:],k-arr[i]-min_distance)
    #ans+=bisect_right(arr[i+1:],k-arr[i]+min_distance)-bisect_left(arr[i+1:],k-arr[i]+min_distance)
  print(count)
      
    #print("result",T,i,start_index,end_index,target,arr[start_index],arr[end_index])

      
      
