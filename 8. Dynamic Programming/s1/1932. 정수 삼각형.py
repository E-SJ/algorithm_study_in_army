import sys
input=sys.stdin.readline
n = int(input())
tri=[(0,)]
dp=[[0]]
for i in range(n):
  tri.append(tuple(map(int,input().split())))
  dp.append([0 for _ in range(0,i+1)])
dp[0][0]=tri[0][0]
dp[1][0]=tri[1][0]

for i in range(2,n+1):
  for j in range(0,i):
    if (j==0):
      dp[i][j]=dp[i-1][j]+tri[i][j]
    elif (j==i-1):
      dp[i][j]=dp[i-1][j-1]+tri[i][j]
    else:
      dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+tri[i][j]

print(max(dp[n]))