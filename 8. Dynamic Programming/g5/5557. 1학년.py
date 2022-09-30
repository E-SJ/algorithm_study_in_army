n = int(input())
arr = [0]+list(map(int,input().split()))
dp=[[0 for _ in range(21)] for _ in range(n)]
dp[0][0]=1
dp[1][arr[1]]=1
for i in range(2,n):
  for j in range(21):

    if (0<=j-arr[i]<=20):
      dp[i][j]+=dp[i-1][j-arr[i]]
    if (0<=j+arr[i]<=20):
      dp[i][j]+=dp[i-1][j+arr[i]]

print(dp[n-1][arr[-1]])