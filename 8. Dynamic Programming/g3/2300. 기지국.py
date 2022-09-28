import sys
import time
input=sys.stdin.readline
n = int(input())
point=[]
for _ in range(n):
  point.append(tuple(map(int,input().split())))
timee=time.time()
point.sort(key=lambda x:(x[0],x[1]))
pointx=list(zip(*point))[0]
pointy=list(zip(*point))[1]
abs_pointx=list(map(abs,pointx))
abs_pointy=list(map(abs,pointy))
#print(point)
dp=[0]*n
dp[0]=abs(point[0][1])*2
for i in range(1,n):
  dp[i] = dp[i-1]+abs(point[i][1])*2
  max_abs_pointy=abs_pointy[i]
  for j in range(i-1,-1,-1): 
    if (j>0):
      max_abs_pointy=max(abs_pointy[j],max_abs_pointy)
      dp[i] = min(dp[i],max(dp[j-1]+max_abs_pointy*2,dp[j-1]+pointx[i]-pointx[j]))
      #print(i,j,dp[i-1]+abs(point[i][1])*2,dp[j-1]+max(list(map(abs,list(zip(*point[j:i+1]))[1])))*2,dp[j-1]+point[i][0]-point[j][0])
    else:
      max_abs_pointy=max(abs_pointy[j],max_abs_pointy)
      dp[i] = min(dp[i],max(max_abs_pointy*2,pointx[i]-pointx[j]))
      #print(i,j,dp[i-1]+abs(point[i][1])*2,max(list(map(abs,list(zip(*point[j:i+1]))[1])))*2,point[i][0]-point[j][0])

print(dp[-1])
#print(time.time()-timee)
#print(*dp)
#print(*abs_pointy)
  
  