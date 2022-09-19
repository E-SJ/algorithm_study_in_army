#기존 풀이
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
"""
# 2차원 dp 풀이(메모리 초과)
import sys
input=sys.stdin.readline
n,k = map(int,input().split())
values=[0]
for _ in range(n):
  values.append(int(input()))
values.sort()
dp=[[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(n+1):
  dp[i][0]=1
for j in range(1,k+1): #0~i까지 동전 사용
  for i in range(1,n+1): #j원
    if (j-values[i]>=0):
      dp[i][j]=dp[i][j-values[i]]+dp[i-1][j]
    else:
      dp[i][j]=dp[i-1][j]
print(dp)
"""

