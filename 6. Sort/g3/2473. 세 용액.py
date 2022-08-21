import sys
input = sys.stdin.readline
n = int(input())
att=sorted([int(x) for x in input().split()])
ans=float("inf")
for pivot in range(n-2):
  point1,point2=pivot+1,n-1
  while point1 < point2:
    p1,p2=att[point1],att[point2]
    temp = p1+p2+att[pivot]
    if (abs(temp)<ans):
        ans=abs(temp)
        left,mid,right=att[pivot],p1,p2
    elif (att[pivot]>=-1):
      print(left,mid,right)
      exit()
    if (temp<0):
      point1+=1
    else:
      point2-=1
    if ans==0:
      print(left,mid,right)
      exit()
print(left,mid,right)