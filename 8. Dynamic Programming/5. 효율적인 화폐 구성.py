import sys
input=sys.stdin.readline
n,m = map(int,input().split())
coins=[]
dp=[10001 for i in range(m+1)]
dp[0]=0
for _ in range(n):
  coins.append(int(input()))
coins.sort(reverse=True)
for i in range(1,m+1):
  for coin in coins:
    if (i-coin>=0):
      dp[i]=min(dp[i],dp[i-coin]+1)
print(-1 if dp[m]==10001 else dp[m])