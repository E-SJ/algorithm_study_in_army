n = int(input())
costs=[tuple()]
for _ in range(n):
  a,b,c = map(int,input().split())
  costs.append([a,b,c])
result=10**9

if (n==2):
  mincases=[costs[1][1]+costs[2][0],costs[1][1]+costs[2][2],costs[1][2]+costs[2][0],costs[1][2]+costs[2][1]]
  result=min(result,min(mincases))
  mincases=[costs[1][0]+costs[2][1],costs[1][0]+costs[2][2],costs[1][2]+costs[2][0],costs[1][2]+costs[2][1]]
  result=min(result,min(mincases))
  mincases=[costs[1][0]+costs[2][1],costs[1][0]+costs[2][2],costs[1][1]+costs[2][0],costs[1][1]+costs[2][2]]
  result=min(result,min(mincases))
  print(result)
  exit()
else:
  for TEST in range(3):
    dp=[0]*(n+1)
    dp_RGB=[-1]*(n+1)
    dp[1]=costs[1][TEST]
    dp_RGB[1]=TEST
    temp = costs[n][TEST]
    costs[n][TEST]=10**9
    for i in range(3,n+1):
      if dp_RGB[i-2]==0:
        mincases=[costs[i-1][1]+costs[i][0],costs[i-1][1]+costs[i][2],costs[i-1][2]+costs[i][0],costs[i-1][2]+costs[i][1]]
        cases=[(1,0),(1,2),(2,0),(2,1)]
        minval=min(mincases)
        minindex=mincases.index(minval)
      elif dp_RGB[i-2]==1:
        mincases=[costs[i-1][0]+costs[i][1],costs[i-1][0]+costs[i][2],costs[i-1][2]+costs[i][0],costs[i-1][2]+costs[i][1]]
        cases=[(0,1),(0,2),(2,0),(2,1)]
        minval=min(mincases)
        minindex=mincases.index(minval)
      elif dp_RGB[i-2]==2:
        mincases=[costs[i-1][0]+costs[i][1],costs[i-1][0]+costs[i][2],costs[i-1][1]+costs[i][0],costs[i-1][1]+costs[i][2]]
        cases=[(0,1),(0,2),(1,0),(1,2)]
        minval=min(mincases)
        minindex=mincases.index(minval)
      dp[i-1]=dp[i-2]+costs[i-1][cases[minindex][0]]
      dp_RGB[i-1]=cases[minindex][0]
      dp[i]=dp[i-1]+costs[i][cases[minindex][1]]
      dp_RGB[i]=cases[minindex][1]
    
    
    #print(dp)
    costs[n][TEST]=temp
    result=min(result,dp[-1])
  
  print(result)