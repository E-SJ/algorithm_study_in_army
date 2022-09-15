n = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)
dp=[10000 for _ in range(n+1)]
dp[0]=0
dp[1]=0
for i in range(1,n+1):
  jump=arr[i]
  for j in range(1,jump+1):
    if (i+j>n):
      break
    dp[i+j]=min(dp[i+j],dp[i]+1)

if (dp[n])==10000:
  print(-1)
else:
  print(dp[n])