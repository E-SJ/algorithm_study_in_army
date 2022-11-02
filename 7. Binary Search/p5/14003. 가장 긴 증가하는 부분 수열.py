from bisect import bisect_left, bisect_right

n = int(input())
arr = [-1000000001]+list(map(int,input().split()))
dp=[0]*(n+1)
bt=[]
to_in_index=bisect_left(bt,(arr[0],0,0))
bt.insert(to_in_index,(arr[0],0,0))
for i in range(1,n+1):
  #max_index=0
  #for j in range(0,i):
  #  if arr[max_index]<arr[j]<arr[i]:
  #    max_index=j
  max_index=bisect_left(bt,(arr[i],999999999,0))-1
  max_index=bt[max_index][2]
  print(bt)
  print(i,max_index)
  print(arr[i],arr[max_index])
  print("")
  dp[i]=bt[max_index][1]+1
  
  to_in_index=bisect_left(bt,(arr[i],dp[i],i))
  bt.insert(to_in_index,(arr[i],dp[i],i))
print(dp)
  