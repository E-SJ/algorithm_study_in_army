import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n=int(input())
matrix=[list(map(int,input().split())) for _ in range(n)]
dy=[0,1,0,-1]
dx=[1,0,-1,0]
def check(num,y,x,minnum,maxnum,trace):
  #print("Checking",y,x,maxnum-minnum>num,y==n-1 and x==n-1,trace)
  if y==n-1 and x==n-1: # 성공조건: 목표지점에 도달했을 떄
    return 1
  flag=False
  temp=0
  for i in range(4):
    ny,nx=y+dy[i],x+dx[i]
    
    if (0<=ny<n and 0<=nx<n and (ny,nx) not in trace and max(maxnum,matrix[ny][nx])-min(minnum,matrix[ny][nx])<num):
      temp = max(temp,check(num,ny,nx,minnum,maxnum,trace|{(ny,nx)}))
      flag=True
  if (flag==False): # 진행되지 못했다면 0 반환
    return 0
    
  else: # 계속 진행되었다면 temp 반환
    return temp

left=0
right=250
ans=right
while left<=right:
  mid = (left+right)//2
  #print("checking",mid,"...")
  visited=[[0 for _ in range(n)] for _ in range(n)]
  result=check(mid,0,0,matrix[0][0],matrix[0][0],{(0,0)})
  if (result==1):
    ans=min(ans,mid)
    right=mid-1
  else:
    left=mid+1
    
print(ans)
  