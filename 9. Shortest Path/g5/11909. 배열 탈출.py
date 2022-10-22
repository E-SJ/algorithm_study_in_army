import sys
input=sys.stdin.readline
n=int(input())
matrix=[]
for _ in range(n):
  matrix.append(list(map(int,input().split())))

dptable=[[10**9 for _ in range(n)] for _ in range(n)]
dptable[0][0]=0
for i in range(n):
  for j in range(n):
    if (0<i<n):
      dptable[i][j]=min(dptable[i][j], dptable[i-1][j]+max(matrix[i][j]-matrix[i-1][j]+1,0))
    if (0<j<n):
      dptable[i][j]=min(dptable[i][j], dptable[i][j-1]+max(matrix[i][j]-matrix[i][j-1]+1,0))
      
print(dptable[n-1][n-1])

# 다익스트라 접근: 실패 (메모리 초과)
"""
import sys
import heapq
input=sys.stdin.readline

n=int(input())
matrix=[]
for _ in range(n):
  matrix.append(list(map(int,input().split())))
graph=[[] for _ in range(n*n)] #i행 j열은 i*n+j 번 노드로 취급 (0행 0열부터 시작)
for i in range(n):
  for j in range(n):
    if (i!=n-1):
      graph[i*n+j].append(((i+1)*n+j,max(matrix[i+1][j]-matrix[i][j]+1,0)))
    if (j!=n-1):
      graph[i*n+j].append((i*n+j+1,max(matrix[i][j+1]-matrix[i][j]+1,0)))
      
for i in range(n):
  del matrix[0]
del matrix

def dijkstra(start,finish):
  global n, graph
  q=[]
  table=[10**4]*(n*n)
  table[0]=0
  heapq.heappush(q,(0,start))
  while q:
    dist,node=heapq.heappop(q)
    if (dist>table[node]):
      continue
    else:
      for adjnode,adjdist in graph[node]:
        if (adjdist+dist<table[adjnode]):
          table[adjnode]=adjdist+dist
          heapq.heappush(q,(adjdist+dist,adjnode))
  return table[finish]

print(dijkstra(0,n*n-1))"""
