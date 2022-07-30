import sys
import math
input=sys.stdin.readline
def print_arr():
  for i in range(n):
    for j in range(m):
      print(arr[i][j],end=" ")
    print()

def revolution(point1,point2):
  
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
  y=point1[0]
  x=point1[1]
  
  
  temp = arr[y][x]
  for _ in range(point2[1]-point1[1]):
    arr[y][x] = arr[y][x+1]
    x+=1
  for _ in range(point2[0]-point1[0]):
    arr[y][x] = arr[y+1][x]
    y+=1
  for _ in range(point2[1]-point1[1]):
    arr[y][x] = arr[y][x-1]
    x-=1
  for _ in range(point2[0]-point1[0]):
    arr[y][x] = arr[y-1][x]
    y-=1
  arr[y+1][x] = temp
    
  

n,m,r = map(int,input().split())
arr = []

for _ in range(n):
  arr.append(list(map(int,input().split())))

point1=[0,0]
point2=[n-1,m-1]
for _ in range(math.ceil(min(n,m)/2)):
  for _ in range(r%(2*(point2[0]-point1[0]+point2[1]-point1[1]))):
    revolution(point1,point2)
  point1[0]+=1
  point1[1]+=1
  point2[0]-=1
  point2[1]-=1

print_arr()