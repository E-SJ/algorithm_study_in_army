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
  print(0)
  exit()
while pos+p<l:
  while i<n:
    if oilbanks[i][0]<=pos+p:
      heapq.heappush(heap,(-oilbanks[i][1],(oilbanks[i][0],oilbanks[i][1])))
      i+=1
    else:
      break
  if (not heap):
    print(-1)
    exit()
  oilbank=heapq.heappop(heap)[1]
  count+=1
  p+=oilbank[1]
  if (pos<oilbank[0]):
    p-=(oilbank[0]-pos)
    pos=oilbank[0]
      
print(count)
      
      


      
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