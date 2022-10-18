import heapq
import sys
input = sys.stdin.readline
n = int(input()) #도시의 개수
m = int(input()) #버스의 개수
graph=[[] for _ in range(n+1)]
for _ in range(m):
  start,end,cost=map(int,input().split())
  graph[start].append((end,cost))
begin,finish = map(int,input().split())

table=[10**8]*(n+1)
table[begin]=0
q=[]
heapq.heappush(q,((0,begin)))
while q:
  dist,node=heapq.heappop(q)
  if dist > table[node]:
    continue
  for adjnode,adjdist in graph[node]:
    if dist+adjdist < table[adjnode]:
      table[adjnode]=dist+adjdist
      heapq.heappush(q,(dist+adjdist,adjnode))

print(table[finish])