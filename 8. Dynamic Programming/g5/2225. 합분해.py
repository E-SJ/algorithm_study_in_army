n,k = map(int,input().split())
dp=[[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(k+1):
  dp[0][i]=1 #dp[합][0~k개더함]
for i in range(1,n+1):
  for j in range(1,k+1):
    dp[i][j] = dp[i][j-1]+dp[i-1][j]

print(dp[n][k]%1000000000)