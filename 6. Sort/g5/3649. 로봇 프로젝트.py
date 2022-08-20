import sys
input=sys.stdin.readline

while True:
  x = input()
  try:
    x = int(x)
  except:
    exit()
  x*= 10000000 #centi to nano
  n = int(input())
  l = []
    
  for _ in range(n):
    l.append(int(input()))
  l.sort()
  if (n<2):
    print("danger")
    continue
  
  point1=0
  point2=n-1
  ans=[]
  while point1!=point2:
    temp=l[point1]+l[point2]
    #print(l[point1],l[point2])
    if (temp==x):
      ans.append((l[point1],l[point2]))
      point2-=1
    elif (temp>x):
      point2-=1
    elif (temp<x):
      point1+=1
  if (len(ans)==0):
    print("danger")
    continue
  ans.sort(key=lambda x:(x[1]-x[0]),reverse=True)
  print("yes",ans[0][0],ans[0][1])
    
    
    
