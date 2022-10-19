import sys
import heapq
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

def dijkstra(start,finish):
  table=[10**9]*(n+1)
  q=[]
  heapq.heappush(q,(0,start))
  table[start]=0
  while q:
    dist,node=heapq.heappop(q)
    if (table[node]<dist):
      continue
    else:
      for adjnode,adjdist in graph[node]:
        if (adjdist+dist<table[adjnode]):
          table[adjnode]=adjdist+dist
          heapq.heappush(q,(adjdist+dist,adjnode))
  return table[finish]

print(dijkstra(1,n))