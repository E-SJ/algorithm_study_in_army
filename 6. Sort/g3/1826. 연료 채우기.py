import sys
input=sys.stdin.readline
n= int(input())
oilbanks=[]
for _ in range(n):
  oilbanks.append(tuple(map(int,input().split())))
l,p = map(int,input().split()) #마을까지의 거리, 연료량
nowp=0 #현재 위치
oilbanks.sort(key=lambda x:(x[0],x[1]))

oilbankindex=0
count=0
i=0
while i<n:
  if (nowp+p>=l):
    print(count)
    exit()
  if (p<0):
    print(-1)
    exit()   
  #print(oilbanks[i][0],nowp,p)
  if (oilbanks[i][0]-nowp<=p):
    if (i+1<n and oilbanks[i+1][0]-nowp<=p):
      #print("DEBUG1")
      if (oilbanks[oilbankindex][1]<oilbanks[i][1]):
        oilbankindex=i
      i+=1
      continue
    else:
      if (oilbanks[oilbankindex][1]<oilbanks[i][1]):
        oilbankindex=i
        #print(i)
      #print("DEBUG3")
      p-=(oilbanks[oilbankindex][0]-nowp)
      p+=oilbanks[oilbankindex][1]
      nowp=oilbanks[oilbankindex][0]
      print(nowp,p)
      i=oilbankindex
      oilbankindex=i+1
      count+=1
      if (nowp+p>=l):
        print(count)
        exit()
      if (p<0):
        print(-1)
        exit()
  else:
    if (nowp+p>=l):
      print(count)
      exit()
    if (p<0):
      print(-1)
      exit()
  i+=1

if (nowp+p>=l):
  print(count)
  exit()
else:
  print(-1)
  exit()