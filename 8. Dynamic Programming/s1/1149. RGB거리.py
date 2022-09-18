import sys
input=sys.stdin.readline
n=int(input())
cost=[(0,0,0)]
for _ in range(n):
  cost.append(tuple(map(int,input().split())))

dp=[[0 for i in range(3)] for i in range(n+1)]
for i in range(1,n+1):
  for j in range(0,3):
    dp[i][j]=min(dp[i-1][(j+1)%3]+cost[i][j],\
                 dp[i-1][(j+2)%3]+cost[i][j],)
print(min(dp[n]))