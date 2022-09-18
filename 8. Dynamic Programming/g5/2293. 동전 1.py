import sys
input=sys.stdin.readline
n,k = map(int,input().split())
values=[0]
for _ in range(n):
  values.append(int(input()))
values.sort()
dp=[0 for _ in range(k+1)]
dp[0]=1
for value in values:
  for i in range(1,k+1):
    if (i-value>=0):
      dp[i]+=dp[i-value]
print(dp[k])