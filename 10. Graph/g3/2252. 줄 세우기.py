from collections import deque
import sys
input=sys.stdin.readline
n,m = map(int,input().split())
graph=[[] for _ in range(n+1)]
degree=[0]*(n+1)
degree[0]=-1
for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  degree[b]+=1
ans=[]
q=deque()

for i in range(len(degree)):
  if degree[i]==0:
    q.append(i)

while q:
  node=q.popleft()
  degree[node]-=1
  ans.append(node)
  for adjnode in graph[node]:
    degree[adjnode]-=1
    if degree[adjnode]==0:
      q.append(adjnode)

print(*ans)

  
  
  