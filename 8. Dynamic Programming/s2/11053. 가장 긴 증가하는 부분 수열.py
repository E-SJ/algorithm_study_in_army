n = int(input())
arr=list(map(int,input().split()))
dp=[0 for _ in range(n+1)]
arr.insert(0,0)
dp[0]=0
dp[1]=1
for i in range(2,n+1):
  maxindex=0
  for j in range(1,i):
    if (arr[j]<arr[i] and dp[maxindex]<dp[j]):
      maxindex=j
  dp[i]=dp[maxindex]+1

print(max(dp))