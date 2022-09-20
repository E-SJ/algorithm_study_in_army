""" # 2차원 dp (시간복잡도↑, 공간복잡도↑)
import sys
input=sys.stdin.readline
n,k = map(int,input().split())
coins=[0]
for _ in range(n):
  coins.append(int(input()))
dp = [[10001 for _ in range(k+1)] for _ in range(n+1)]
for i in range(n+1):
  dp[i][0]=0
for i in range(1,n+1):
  for j in range(1,k+1):
    dp[i][j]=dp[i-1][j]
    for l in range(1,i+1):
      if (j-coins[l]>=0):
        dp[i][j]=min(dp[i][j],dp[i][j-coins[l]]+1)

if dp[n][k]==10001:
  print(-1)
else:
  print(dp[n][k])
"""

import sys
input=sys.stdin.readline
n,k = map(int,input().split())
coins=[0]
for _ in range(n):
  coins.append(int(input()))
dp = [10001 for _ in range(k+1)]

dp[0]=0
for j in range(1,k+1):
  for coin in coins:
    if (j-coin>=0):
      dp[j]=min(dp[j],dp[j-coin]+1)

if dp[k]==10001:
  print(-1)
else:
  print(dp[k])
