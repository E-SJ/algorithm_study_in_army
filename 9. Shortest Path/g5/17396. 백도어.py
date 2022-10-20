import sys
import heapq
input=sys.stdin.readline
n,m = map(int,input().split())
sight=list(map(int,input().split()))
graph=[[] for _ in range(n)]
for _ in range(m):
  a,b,t = map(int,input().split())
  #if not (a!=n-1 and b!=n-1 and (sight[a]==1 or sight[b]==1)):
  graph[a].append((b,t))
  graph[b].append((a,t))

table=[10**11]*n
table[0]=0
q=[]
heapq.heappush(q,(0,0))
while q:
  dist,node=heapq.heappop(q)
  if dist>table[node]:
    continue
  else:
    for adjnode,adjdist in graph[node]:
      if adjdist+dist<table[adjnode] and (sight[adjnode]==0 or adjnode==n-1):
        table[adjnode]=adjdist+dist
        heapq.heappush(q,(adjdist+dist,adjnode))

#print(graph)
#print(table)
ans = table[n-1]
if (ans==10**11):
  print(-1)
else:
  print(ans)