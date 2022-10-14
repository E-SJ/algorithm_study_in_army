from bisect import bisect_left, bisect_right
import sys
input=sys.stdin.readline
n,c = map(int,input().split())
weights=list(map(int,input().split()))
weights.sort()


#1개 탐색 (이진탐색)
if (0<=bisect_left(weights,c)<n and weights[bisect_left(weights,c)]==c):
  print(1)
  exit()
if (n==1):
  print(0)
  exit()

#2~3개 탐색 (투포인터+이진탐색)
p1=0
p2=n-1
while p1<p2:
  if (weights[p1]+weights[p2]>c):
    p2-=1
  elif (weights[p1]+weights[p2]<c):
    if (p1>0 and 0<=bisect_left(weights[:p1],c-weights[p1]-weights[p2])<p1 and weights[bisect_left(weights[:p1],c-weights[p1]-weights[p2])]==c-weights[p1]-weights[p2]):
      print(1)
      exit()
    p1+=1
  else:
    print(1)
    exit()
print(0)



"""
#2개 탐색 (투포인터)
p1=0
p2=n-1
while p1<p2:
  if (weights[p1]+weights[p2]>c):
    p2-=1
  elif (weights[p1]+weights[p2]<c):
    p1+=1
  else:
    print(1)
    exit()
if (n==2):
  print(0)
  exit()
  
#3개 탐색 (투포인터)
for i in range(n-2):
  p1=i+1
  p2=n-1
  while p1<p2:
    if (weights[i]+weights[p1]+weights[p2]>c):
      p2-=1
    elif (weights[i]+weights[p1]+weights[p2]<c):
      p1+=1
    else:
      print(1)
      exit()
print(0)
"""
