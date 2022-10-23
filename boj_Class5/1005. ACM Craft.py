import sys
from collections import deque
input=sys.stdin.readline

def topological_sort(n,order,degrees):
  q=deque()
  for i in range(1,n+1):
    if degrees[i]==0:
      q.append(i)
  result=[]
  while q:
    node=q.popleft()
    result.append(node)
    degrees[node]-=1
    for adjnode in order[node]:
      degrees[adjnode]-=1
      if degrees[adjnode]==0:
        q.append(adjnode)
  return result
      
t=int(input())

for _ in range(t):
  n,k = map(int,input().split())
  delay=[0]+list(map(int,input().split()))
  order=[[] for _ in range(n+1)]
  previous_order=[[] for _ in range(n+1)]
  degrees=[0]*(n+1)
  degrees[0]=-1
  for _ in range(k):
    a,b = map(int,input().split())
    order[a].append(b)
    previous_order[b].append(a)
    degrees[b]+=1
    
  w=int(input())
  dptable=[0]*(n+1)
  ans=0
  topology=topological_sort(n,order,degrees)

  for item in topology:
    dptable[item]=delay[item]
    maxvalue=0
    for preceded_node in previous_order[item]:
      maxvalue=max(maxvalue,dptable[preceded_node])
    dptable[item]+=maxvalue
    if item==w:
      break
    
  print(dptable[w])
    


""" DFS 풀이 -> DP로 바꾸기
import sys
from bisect import bisect_left as bs
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
t=int(input())

def dfs(now):
  global order
  global w,k
  time=delay[now]
  if (now==w):
    return time
  index=bs(order,(now,))
  temp=0
  while (index<=k and order[index][0]==now):
    temp=max(temp,dfs(order[index][1]))
    index+=1
  return time+temp
  
for _ in range(t):
  n,k = map(int,input().split())
  delay=[0]+list(map(int,input().split()))
  order=[(0,0)]+[tuple(map(int,input().split())) for _ in range(k)]
  order.sort()
  w=int(input())
  startcase={i for i in range(1,n+1)}-set(list(zip(*order))[1])
  ans=10**12
  for case in startcase:
    ans=min(ans,dfs(case))
  print(ans)
"""