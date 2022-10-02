import sys
input=sys.stdin.readline
n = int(input())
arr=[tuple(map(int,input().split())) for _ in range(n)]
dp=[[2**31 for _ in range(n)] for _ in range(n)]
for i in range(0,n):
  dp[i][i]=0
for i in range(0,n-1):
  dp[i][i+1] = arr[i][0]*arr[i][1]*arr[i+1][1]
for k in range(2,n):
  for i in range(0,n-k):
    for j in range(i,i+k):
      dp[i][i+k] = min(dp[i][i+k],dp[i][j]+dp[j+1][i+k]+arr[i][0]*arr[j][1]*arr[i+k][1])
#dp[0][2] = min(dp[0][1]+arr[0][0]*arr[2][0]*arr[2][1] , dp[1][2]+arr[0][0]*arr[0][1]*arr[2][1])
#dp[1][3] = min(dp[1][2]+arr[1][0]*arr[3][0]*arr[3][1] , dp[2][3]+arr[1][0]*arr[1][1]*arr[3][1])
#dp[0][3] = min(dp[0][2]+arr[0][0]*arr[3][0]*arr[3][1] , dp[1][3]+arr[0][0]*arr[0][1]*arr[3][1], dp[0][1]+dp[2][3]+arr[0][0]*arr[1][1]*arr[3][1])
print(dp[0][n-1])
#print(*dp,sep='\n')
#for i in range(1,n):
  