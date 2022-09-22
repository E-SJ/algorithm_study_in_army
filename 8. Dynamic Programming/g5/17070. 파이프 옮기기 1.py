import sys
input=sys.stdin.readline
n = int(input())
wall = []
wall.append(tuple([0 for _ in range(n+1)]))
for _ in range(n):
  wall.append(tuple([0]+list(map(int,input().split()))))


dp = [[[0 for _ in range(3)] for _ in range(n+1)] for _ in range(n+1)]
dp[1][2][0]=1
#dp[행][열][0:- 1:\ 2:|]
for i in range(1,n+1):
  for j in range(1,n+1):
    if (wall[i][j]==0):
      dp[i][j][0]+=(dp[i][j-1][0]+dp[i][j-1][1])
      dp[i][j][2]+=(dp[i-1][j][1]+dp[i-1][j][2])
      if (wall[i-1][j]==0 and wall[i][j-1]==0):
        dp[i][j][1]+=(dp[i-1][j-1][0]+dp[i-1][j-1][1]+dp[i-1][j-1][2])

#print(*wall,sep="\n")
#print(*dp,sep="\n")
print(sum(dp[n][n]))