import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
  n=int(input())
  coins = list(map(int,input().split()))
  m=int(input())
  dp=[0]*(m+1)
  for i in range(coins[0],m+1):
    for j in range(len(coins)):
      if i-coins[j]>=0:
        dp[i]=max(dp[i],dp[i-coins[j]]+1)

  print(dp)
    
  