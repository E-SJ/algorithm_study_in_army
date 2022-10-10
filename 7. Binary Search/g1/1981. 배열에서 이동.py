from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
matrix=[list(map(int,input().split())) for _ in range(n)]
dy=[0,1,0,-1]
dx=[1,0,-1,0]
def check(minnum,maxnum):
  visited=[[0 for _ in range(n)] for _ in range(n)]
  q=deque()
  q.append((0,0))
  if not minnum<=matrix[0][0]<=maxnum:
    return 0
  while q:
    for _ in range(len(q)):
      y,x = q.popleft()
      if (y==n-1 and x==n-1):
        return 1
      for i in range(4):
        ny,nx=y+dy[i],x+dx[i]
        if (0<=ny<n and 0<=nx<n and visited[ny][nx]==0 and minnum<=matrix[ny][nx]<=maxnum):
          visited[ny][nx]=1
          q.append((ny,nx))
  return 0


left=0
right=200
ans=right
while left<=right:
  mid = (left+right)//2
  result=0
  for i in range(0,201-mid):
    result=max(result,check(i,i+mid))
  if (result==1):
    ans=min(ans,mid)
    right=mid-1
  else:
    left=mid+1
    
print(ans)

