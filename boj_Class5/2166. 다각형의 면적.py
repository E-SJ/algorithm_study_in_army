import sys
input=sys.stdin.readline
n=int(input())
points=[]
for _ in range(n):
  x,y=map(int,input().split())
  points.append((y,x))
points.append(points[0])
ans1=0
for i in range(n):
  ans1+=points[i][0]*points[i+1][1]
ans2=0
for i in range(n):
  ans2+=points[i][1]*points[i+1][0]
ans=abs(ans1-ans2)/2

print(round(ans,1))