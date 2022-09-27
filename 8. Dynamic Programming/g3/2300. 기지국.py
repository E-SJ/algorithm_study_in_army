import sys
input=sys.stdin.readline
n = int(input())
point=[]
for _ in range(n):
  point.append(tuple(map(int,input().split())))
point.sort(key=lambda x:(x[0],x[1]))
#print(point)
dp=[0 for _ in range(n)]
dp[0]=abs(point[0][1])*2
for i in range(1,n):
  dp[i] = dp[i-1]+abs(point[i][1])*2
  for j in range(i-1,-1,-1): 
    if (i>1):
      dp[i] = min(dp[i],max(dp[j-1]+max(list(map(abs,list(zip(*point[j:i+1]))[1])))*2,dp[j-1]+point[i][0]-point[j][0]))
      #print(i,j,dp[i-1]+abs(point[i][1])*2,dp[j-1]+max(list(map(abs,list(zip(*point[j:i+1]))[1])))*2,dp[j-1]+point[i][0]-point[j][0])
    else:
      dp[i] = min(dp[i],max(max(list(map(abs,list(zip(*point[j:i+1]))[1])))*2,point[i][0]-point[j][0]))
      #print(i,j,dp[i-1]+abs(point[i][1])*2,max(list(map(abs,list(zip(*point[j:i+1]))[1])))*2,point[i][0]-point[j][0])

print(dp[-1])
  
  