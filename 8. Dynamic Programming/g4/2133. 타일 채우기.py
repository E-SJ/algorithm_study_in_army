"""
n = int(input())
dp=[0 for _ in range(n+1)]
dp[0]=1
if (n>=2):
  dp[2]=3
for i in range(4,n+1):
  dp[i]+=dp[i-2]*3
  for j in range(4,i+1,2):
    dp[i]+=dp[i-j]*2
print(dp[n])
"""
# 숏코딩 도전
d=[1,0]*16
for i in range(2,31,2):d[i]=d[i-2]+sum(d[:i])*2
print(d[int(input())])
#81B , 10등!