import sys
input=sys.stdin.readline
t = int(input())
for T in range(t):
  n,k = map(int,input().split())
  arr = list(map(int,input().split()))
  arr.sort()
  for i in range(n):
    if (arr[i]>k):
      break
    else:
      target=k-arr[i]
      
      left=i+1
      right=n-1
      while left<right:
        mid=(left+right)//2
        if mid>target:
          right=mid-1
        elif mid<target:
          left=mid+1
        else:
          while mid-1>i and arr[mid]==arr[mid-1]:
            mid-=1
          break
      start_index=mid
      
      left=i+1
      right=n-1
      while left<right:
        mid=(left+right)//2
        if mid>target:
          right=mid-1
        elif mid<target:
          left=mid+1
        else:
          while mid+1<n and arr[mid]==arr[mid+1]:
            mid+=1
          break
      end_index=mid
    print("result",T,i,start_index,end_index,target,arr[start_index],arr[end_index])

      
      
