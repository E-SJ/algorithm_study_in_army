import heapq
import sys
input=sys.stdin.readline
n,m,k,x = map(int,input().split()) #도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
graph=[[] for _ in range(n+1)]

for _ in range(m):
  start,end = map(int,input().split())
  graph[start].append((end,1)) #graph[출발 노드]=[(도착 노드,가중치), ...]
table=[10**9]*(n+1)
heap=[]
heapq.heappush(heap,(0,x)) #가중치, 노드
table[x]=0
while heap:
  dist,node=heapq.heappop(heap)
  if table[node]<dist:
    continue
  else:
    for adjnode,adjdist in graph[node]:
      if dist+adjdist<table[adjnode]:
        table[adjnode]=dist+adjdist
        heapq.heappush(heap,(dist+adjdist,adjnode))

ans=[]
for i in range(len(table)):
  if table[i]==k:
    ans.append(i)
if (len(ans)==0):
  print(-1)
else:
  print(*ans,sep="\n")
    