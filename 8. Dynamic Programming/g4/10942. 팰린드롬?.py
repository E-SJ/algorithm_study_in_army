import sys
sys.setrecursionlimit(2000)
input=sys.stdin.readline
n = int(input())
arr = [0]+list(map(int,input().split()))
m = int(input())
quest=[]
for _ in range(m):
  quest.append(tuple(map(int,input().split())))
dp=[[-1 for _ in range(n+1)] for _ in range(n+1)]

#top-down은 시간 초과. bottom-up 방식으로 재시도해보자.
"""
def returndp(a,b):
  if (dp[a][b]==-1):
    dp[a][b]=int(returndp(a+1,b-1) and arr[a]==arr[b])
  return dp[a][b]
for i in range(1,n+1):
  for j in range(i,min(i+2,n+1)):
    if i==j:
      dp[i][j]=1
    else:
      dp[i][j]=int(arr[i]==arr[j])
for i in range(1,n+1):
  for j in range(i+2,n+1):
    dp[i][j]=returndp(i,j)
"""

#bottom-up
for offset in range(0,n):
  for i in range(1,n-offset+1):
    if offset==0:
      dp[i][i]=1
    elif offset==1:
      dp[i][i+1]=int(arr[i]==arr[i+1])
    else:
      dp[i][i+offset]=min(dp[i+1][i+offset-1],int(arr[i]==arr[i+offset]))
    

for s,e in quest:
  print(dp[s][e])
