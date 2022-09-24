n = int(input())
arr=list(map(int,input().split()))
arr.insert(0,0)
dp=[[0,0] for _ in range(n+1)] #dp[~번째 숫자까지][0:증가 1:감소]
dp[0][0]=0
dp[0][1]=0
for i in range(1,n+1):
  maxindex=0
  arr[0]=0
  for j in range(0,i):
    if (dp[maxindex][0]<dp[j][0] and arr[j]<arr[i]):
      maxindex=j
  dp[i][0]=dp[maxindex][0]+1

  
  minindex=0
  arr[0]=1001
  for j in range(0,i):
    if (dp[minindex][1]<dp[j][1]  and arr[j]>arr[i]):
      minindex=j

  dp[i][1]=max(dp[minindex][1]+1,dp[i][0])

print(max(list(zip(*dp))[1]))