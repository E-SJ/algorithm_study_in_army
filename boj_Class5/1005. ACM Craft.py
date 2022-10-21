import sys
from bisect import bisect_left as bs
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
t=int(input())

def dp(start,end):
  global order,delay
  global w,k,n
  table=[0]*(n+1)
  table[start]=delay[start]
  for i in range(start+1,end+1):
    temp=0
    for j in range(order[i]):
      temp=max(temp,delay[j])
  
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
  order=[[] for _ in range(n+1)]
  for _ in range(k):
    a,b = map(int,input().split())
    order[b].append(a)
  w=int(input())
  


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