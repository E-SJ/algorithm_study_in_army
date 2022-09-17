n=int(input())
loss=list(map(int,input().split()))
get=list(map(int,input().split()))
loss.insert(0,0)
get.insert(0,0)

dp=[[0 for _ in range(100)] for _ in range(n+1)]


for i in range(1,n+1):
  for j in range(1,100):
    if j-loss[i]>=0:
      dp[i][j]=max(dp[i-1][j],dp[i-1][j-loss[i]]+get[i])
    else:
      dp[i][j]=dp[i-1][j]
print(dp[n][99])