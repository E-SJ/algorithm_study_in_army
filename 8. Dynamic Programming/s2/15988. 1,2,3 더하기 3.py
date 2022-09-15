import sys
input=sys.stdin.readline
t = int(input())
cases=[]
for _ in range(t):
  cases.append(int(input()))
maxcase=max(cases)
dp=[0 for _ in range(maxcase+1)]
dp[1]=1
dp[2]=2
dp[3]=4
for i in range(4,maxcase+1):
  dp[i]=dp[i-3]%1000000009+dp[i-2]%1000000009+dp[i-1]%1000000009

for case in cases:
  print(dp[case]%1000000009)

#print(dp)