""" 풀다보니 queue로 풀게 되었다. 이걸 의도한 문제가 아닌 것 같은데..?
from collections import deque
queue=deque()
x = int(input())
queue.append(x)
count=0
cache=[0 for i in range(30000)]
while queue:
  for _ in range(len(queue)):
    x=queue.popleft()
    if x==1:
      break
    if x%5==0 and cache[x//5]==0:
      cache[x//5]=1
      queue.append(x//5)
    if x%3==0 and cache[x//3]==0:
      cache[x//3]=1
      queue.append(x//3)
    if x%2==0 and cache[x//2]==0:
      cache[x//2]=1
      queue.append(x//2)
    if cache[x-1]==0:
      cache[x-1]=1
      queue.append(x-1)
  if (x==1):
    break
  count+=1
print (count)
"""
import sys
sys.setrecursionlimit(100000)
x = int(input())
ans=999999999999999
count=0
def solve(x):
  global count,ans
  if x==1:
    ans=min(ans,count)
    count=0
  else:
    count+=1
    if x%5==0:
      solve(x//5)
    if x%3==0:
      solve(x//3)
    if x%2==0:
      solve(x//2)
    solve(x-1)
solve(x)

print(ans)