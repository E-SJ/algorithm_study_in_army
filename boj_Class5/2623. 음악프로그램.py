from collections import deque
import sys

input=sys.stdin.readline
n,m = map(int,input().split())
order=[[] for _ in range(n+1)]
for _ in range(m):
  temp_order=list(map(int,input().split()))[1:]
  for i,item in enumerate(temp_order):
    if (i!=0 and not temp_order[i-1] in order[item]):
      order[item].append(temp_order[i-1])
#print(order)

indegrees=[len(adj) for adj in order]
#print(indegrees)
q=deque()
for i,indegree in enumerate(indegrees):
  if (indegree==0):
    q.append(i)
ans=[]
while q:
  for _ in range(len(q)):
    node = q.popleft()
    ans.append(node)
    for i,adj in enumerate(order):
      if node in adj:
        adj.remove(node)
        indegrees[i]-=1
        if indegrees[i]==0:
          q.append(i)

ans.remove(0)
if (len(ans)!=n):
  print(0)
else:
  print(*ans,sep='\n')
      