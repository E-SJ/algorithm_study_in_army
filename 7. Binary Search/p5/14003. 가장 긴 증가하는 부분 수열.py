from bisect import bisect_left, bisect_right

n = int(input())
arr = [-1000000001]+list(map(int,input().split()))
dp=[0]*(n+1)

for i in range(1,n+1):
  max_index=0
  for j in range(0,i):
    if (dp[max_index]<dp[j] and arr[j]<arr[i]):
      max_index=j
  dp[i]=dp[max_index]+1

  
print(max(dp))
max_dp=max(dp)
ans=[]
for i in range(n,0,-1):
  if dp[i]==max_dp:
    ans.insert(0,arr[i])
    max_dp-=1
    continue
print(*ans)