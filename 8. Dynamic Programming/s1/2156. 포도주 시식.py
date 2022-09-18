import sys
input=sys.stdin.readline
n=int(input())
amounts=[0]
for _ in range(n):
  amounts.append(int(input()))
dp=[0 for _ in range(n+1)]
dp[1]=amounts[1]
if n>1:
  dp[2]=dp[1]+amounts[2]
for i in range(3,n+1):
  dp[i]=max(dp[i-3]+amounts[i-1]+amounts[i],\
            dp[i-2]+amounts[i],\
            dp[i-1])

print(dp[n])
