import sys
input=sys.stdin.readline
n = int(input())
lines=[]
for _ in range(n):
  lines.append(tuple(map(int,input().split())))
lines.sort(key=lambda x:x[0])
lines.insert(0,(-1,-1))
dp=[0 for _ in range(n+1)]

for i in range(1,n+1):
  maxindex=0
  for j in range(1,i):
    if lines[i][1]>lines[j][1] and dp[maxindex]<=dp[j]:
      maxindex=j
  dp[i]=dp[maxindex]+1
print(n-max(dp))