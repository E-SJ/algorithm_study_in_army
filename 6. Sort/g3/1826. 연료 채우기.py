import heapq
import sys
input=sys.stdin.readline
n= int(input())
oilbanks=[]
for _ in range(n):
  oilbanks.append(tuple(map(int,input().split())))
l,p = map(int,input().split()) #마을까지의 거리, 연료량
oilbanks.sort(key=lambda x:(x[0],x[1]))
pos = 0
heap=[]
i=0
count=0
if (pos+p>=l):
  print(count)
  exit()
while True:
  if (i<n):
    heapq.heappush(heap,(-oilbanks[i][1],(oilbanks[i][0],oilbanks[i][1])))
    p-=(oilbanks[i][0]-pos)
    pos = oilbanks[i][0]
  elif not heap:
    print(-1)
    exit()
  #print(heap,pos,p)
  if (i+1<n and oilbanks[i+1][0]-pos<=p):
    i+=1
    continue
  elif (heap):
    #print('debug')
    oilbank=heapq.heappop(heap)[1]
    p+=oilbank[1]
    count+=1
  else:
    print(-1)
    exit()
  #print(heap,pos,p)
  if (pos+p>=l):
    print(count)
    exit()
  i+=1
print(-1)
  
      
      
      
      


      
""" 잘못된 알고리즘: 폐기
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

"""