import sys
input=sys.stdin.readline
from itertools import combinations
import math
T=int(input())
for _ in range(T):
  points=[]
  n = int(input())
  sum_x=0
  sum_y=0
  for _ in range(n):
    x,y = map(int,input().split())
    points.append((x,y))
    sum_x+=x
    sum_y+=y
  #vectors=[]
  ans=100000000
  for pts in combinations(points,n//2):
    #positive_pts=list(pts)
    #negative_pts=list(set(points)-set(positive_pts))
    #print(positive_pts,negative_pts)
    temp_axis1=0
    temp_axis2=0
    for p in pts:
      temp_axis1+=p[0]
      temp_axis2+=p[1]
    temp_axis1-=sum_x-temp_axis1
    temp_axis2-=sum_y-temp_axis2
    ans=min(ans,math.sqrt(temp_axis1**2+temp_axis2**2))
  print(ans)