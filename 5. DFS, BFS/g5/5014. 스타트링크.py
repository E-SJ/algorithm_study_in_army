f,s,g,u,d = map(int,input().split()) #총 f층, s층에 강호가 있음, g층에 사무실
from collections import deque
from math import gcd
def lcm(a,b):
  if (a*b!=0):
    return a*b//gcd(a,b)
  else:
    return 0

def bfs(s):
  Q.append(s)
  count=0
  while len(Q):
    for _ in range(len(Q)):
      node=Q.popleft()
      if visited[node] == 1:
        continue
      visited[node]=1
      if (node!=g):
        if (node+u<=f and node+u<=g+lcm(u,d)):
          if (visited[node+u]!=1 and not node+u in Q):
            Q.append(node+u)
        if (node-d>=1 and node-d>=g-lcm(u,d)):
          if (visited[node-d]!=1 and not node-d in Q):
            Q.append(node-d)
      
      if (node==g):
        return count
    #print(Q)
    count+=1
  return "use the stairs"

Q=deque()
visited=[0 for _ in range(f+d+1)]
print(bfs(s))