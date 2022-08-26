import sys
input=sys.stdin.readline
n=int(input())
flowers=[]
for _ in range(n):
  sm,sd,em,ed = map(int,input().split())
  flowers.append((sm,sd,em,ed))
flowers.sort(key=lambda x:(x[0],x[1],-x[2],-x[3]))

mon_max,day_max=1,1
for flower in flowers:
  if (flower[0]==1 or flower[0]==2 or (flower[0]==3 and flower[1]==1)):
    if (flower[0]>mon_max):
      mon_max=flower[0]
      if (flower[1]>day_max):
        day_max=flower[1]
  else:
    