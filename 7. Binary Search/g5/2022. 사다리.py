x,y,c = map(float,input().split())
from math import sqrt
left=0
right=3000000000
while left<=right:
  mid=(left+right)/2
  #print("try",mid)
  if (x**2-mid**2>=0 and y**2-mid**2>=0):
    temp=(sqrt(x**2-mid**2)*sqrt(y**2-mid**2))/(sqrt(y**2-mid**2)+sqrt(x**2-mid**2))
    if c-0.0001<temp<c+0.0001:
      print(mid)
      exit()
    elif (temp>c+0.0001):
      left=mid
    elif (temp<c-0.0001):
      right=mid
  else:
    right=mid
  