from collections import deque
n,m =map(int,input().split())
ladders=[]
snakes=[]
position=[[],[]]
Q=deque()
visit=[0 for _ in range(101)]
  
for _ in range(n):
  a,b = tuple(map(int,input().split()))
  position[0].append(a)
  position[1].append(b)

for _ in range(m):
  a,b = tuple(map(int,input().split()))
  position[0].append(a)
  position[1].append(b)
  
def move(pos):
  if (pos in position[0]):
    return position[1][position[0].index(pos)]
  return pos


def dice():
  count=0
  Q.append(1)
  visit[1]=1
  while (len(Q)):
    for i in range(len(Q)):
      pos = Q.popleft()
      if (pos==100):
        print(count)
        exit()
      for i in range(1,7):
        afterpos = move(pos+i)
        if (1<=afterpos<=100 and visit[afterpos]==0):
          Q.append(afterpos)
          visit[afterpos]=1
    count+=1
dice()

