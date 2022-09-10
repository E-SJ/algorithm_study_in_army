n = int(input())
dp=[0 for _ in range(n)]
base=list(map(int,input().split()))
dp[0]=base[0]
dp[1]=max(base[0],base[1])
for i in range(2,n):
  dp[i]=max(dp[i-2]+base[i],dp[i-1])

print(dp[n-1])