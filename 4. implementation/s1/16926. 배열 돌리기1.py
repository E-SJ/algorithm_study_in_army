import sys
import math
input=sys.stdin.readline
from collections import deque
def print_arr():
  for i in range(n):
    for j in range(m):
      print(arr[i][j],end=" ")
    print()

def revolution(point1,point2,rev):
  
  """
  for i in range(2*(point2[0]-point1[0]+point2[1]-point1[1])):
    pos.append([y,x])
    if (x==point2[1] and y==point1[0]):
      x-=1
    elif (x==point1[1] and y==point2[0]):
      x+=1
    elif (x==point2[1] and y==point2[0]):
      y-=1
    elif (x==point1[1] and y==point1[0]):
      y+=1
    elif (x!=point1[1] and y==point2[0]):
      x+=1
    elif (x==point2[1] and y!=point2[0]):
      y-=1
    elif (x==point1[1] and y!=point2[0]):
      y+=1
    elif (x!=point2[1] and y==point1[0]):
      x-=1
  pos.reverse()
  """
  queue=deque()
  y=point1[0]
  x=point1[1]
  for _ in range(point2[1]-point1[1]):
    queue.append(arr[y][x])
    x+=1
  for _ in range(point2[0]-point1[0]):
    queue.append(arr[y][x])
    y+=1
  for _ in range(point2[1]-point1[1]):
    queue.append(arr[y][x])
    x-=1
  for _ in range(point2[0]-point1[0]):
    queue.append(arr[y][x])
    y-=1
  queue.rotate(-rev)
  y=point1[0]
  x=point1[1]
  for _ in range(point2[1]-point1[1]):
    arr[y][x] = queue.popleft()
    x+=1
  for _ in range(point2[0]-point1[0]):
    arr[y][x] = queue.popleft()
    y+=1
  for _ in range(point2[1]-point1[1]):
    arr[y][x] = queue.popleft()
    x-=1
  for _ in range(point2[0]-point1[0]):
    arr[y][x] = queue.popleft()
    y-=1
  #arr[y+1][x] = temp
    
  

n,m,r = map(int,input().split())
arr = []

for _ in range(n):
  arr.append(list(map(int,input().split())))

point1=[0,0]
point2=[n-1,m-1]
for _ in range(math.ceil(min(n,m)/2)):
  revolution(point1,point2,r%(2*(point2[0]-point1[0]+point2[1]-point1[1])))
  point1[0]+=1
  point1[1]+=1
  point2[0]-=1
  point2[1]-=1

print_arr()