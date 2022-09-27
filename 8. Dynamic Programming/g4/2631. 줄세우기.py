import sys
input=sys.stdin.readline
n=int(input())
people=[0]
for _ in range(n):
  people.append(int(input()))
dp=[0 for _ in range(n+1)]
for i in range(1,n+1):
  maxindex=0
  for j in range(0,i):
    if (dp[maxindex]<dp[j] and people[j]<people[i]):
      maxindex=j
  dp[i]=dp[maxindex]+1
print(n-max(dp))
