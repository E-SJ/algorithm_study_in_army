n = int(input())
arr=[1001]+list(map(int,input().split()))
dp=[0 for _ in range(n+1)]
dp[1]=1
for i in range(2,n+1):
  maxindex=0
  for j in range(1,i):
    if (dp[maxindex]<dp[j] and arr[i]>arr[j]):
      maxindex=j
  dp[i]=dp[maxindex]+1
  
dpitem=max(dp)
ans=[]
for i in range(n,0,-1):
  if dpitem==dp[i]:
    ans=[arr[i]]+ans
    dpitem-=1
    
print(max(dp))
print(*ans)