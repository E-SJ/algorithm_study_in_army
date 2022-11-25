import sys
import heapq
from time import time

def find(table,node):
  if (table[node]!=node):
    table[node]=find(table,table[node])
  return table[node]
  
def union(table,node1,node2):
  parent_node1=find(table,node1)
  parent_node2=find(table,node2)
  if (parent_node1>parent_node2):
    table[parent_node1]=parent_node2
  else:
    table[parent_node2]=parent_node1
    
def distance(planet1,planet2):
  return min(abs(planets[planet1][0]-planets[planet2][0]),abs(planets[planet1][1]-planets[planet2][1]),abs(planets[planet1][2]-planets[planet2][2]))

  
input=sys.stdin.readline
n = int(input())
planets=[]
for i in range(n):
  planets.append((tuple(map(int,input().split()))+(i,)))
table=[i for i in range(n)]

planets_sort=[]
for axis in range(3):
  planets_sort.append(sorted(planets,key=lambda x:(x[axis])))

q=[]
for axis in range(3):
  for i in range(n-1):
    heapq.heappush(q,(distance(planets_sort[axis][i][3],planets_sort[axis][i+1][3]),planets_sort[axis][i][3],planets_sort[axis][i+1][3]))

#print(q)
ans = 0
#t=time()
while q:
  dist,i,j=heapq.heappop(q)
  if find(table,i)!=find(table,j):
    union(table,i,j)
    ans+=distance(i,j)
    #print(ans)

print(ans)
#print(time()-t)