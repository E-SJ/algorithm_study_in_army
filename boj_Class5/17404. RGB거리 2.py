INF=10**9
n = int(input())
costs=[tuple()]
for _ in range(n):
  a,b,c = map(int,input().split())
  costs.append([a,b,c])
result=10**9

if (n==2):
  mincases=[costs[1][0]+costs[2][1],costs[1][0]+costs[2][2],costs[1][1]+costs[2][0],costs[1][1]+costs[2][2],costs[1][2]+costs[2][0],costs[1][2]+costs[2][1]]
  print(min(mincases))
  exit()
else:
  for TEST in range(3):
    dp=[[0,0,0] for _ in range(n+1)]
    dp[1]=[INF,INF,INF]
    dp[1][TEST]=costs[1][TEST]
    for i in range(2,n+1):
      dp[i][0]=min(dp[i-1][1],dp[i-1][2])+costs[i][0]
      dp[i][1]=min(dp[i-1][0],dp[i-1][2])+costs[i][1]
      dp[i][2]=min(dp[i-1][1],dp[i-1][0])+costs[i][2]
    if (TEST==0):
      result=min(result,dp[n][1],dp[n][2])
    elif (TEST==1):
      result=min(result,dp[n][0],dp[n][2])
    elif (TEST==2):
      result=min(result,dp[n][0],dp[n][1])
     
  
  print(result)