import sys
input = sys.stdin.readline
n = int(input())
lines=[(0,0,0)]
dp_max=[0,0,0]
dp_min=[0,0,0]
for _ in range(n):
  lines.append(tuple(map(int,input().split())))

for i in range(1,n+1):
  temp=[0,0,0]
  temp[0]=max(dp_max[0],dp_max[1])+lines[i][0]
  temp[1]=max(dp_max[0],dp_max[1],dp_max[2])+lines[i][1]
  temp[2]=max(dp_max[1],dp_max[2])+lines[i][2]
  dp_max[0]=temp[0]
  dp_max[1]=temp[1]
  dp_max[2]=temp[2]

  temp=[0,0,0]
  temp[0]=min(dp_min[0],dp_min[1])+lines[i][0]
  temp[1]=min(dp_min[0],dp_min[1],dp_min[2])+lines[i][1]
  temp[2]=min(dp_min[1],dp_min[2])+lines[i][2]
  dp_min[0]=temp[0]
  dp_min[1]=temp[1]
  dp_min[2]=temp[2]
  

print(max(dp_max),min(dp_min))