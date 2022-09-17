import sys
input=sys.stdin.readline
n,m=map(int,input().split())
chapters=[(0,0)]
for _ in range(m):
  chapters.append(tuple(map(int,input().split())))

dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
#dp[챕터수][기한]
for i in range(1,m+1):
  for j in range(1,n+1):
    if j-chapters[i][0]>=0:
      dp[i][j]=max(dp[i-1][j],dp[i-1][j-chapters[i][0]]+chapters[i][1])
    else:
      dp[i][j]=dp[i-1][j]

print(dp[m][n])