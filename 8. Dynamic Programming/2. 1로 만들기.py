# 풀다보니 queue로 풀게 되었다. 이걸 의도한 문제가 아닌 것 같은데..?
"""
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

# 평범한 재귀함수 구현. 시간복잡도가 매우 크다.
""" 
import sys
sys.setrecursionlimit(100000)
x = int(input())

def solve(x):
  if x==1:
    return 0
  else:
    ans = solve(x-1)+1
    if x%5==0:
      ans = min(ans,solve(x//5)+1)
    if x%3==0:
      ans = min(ans,solve(x//3)+1)
    if x%2==0:
      ans = min(ans,solve(x//2)+1)
    return ans
print(solve(x))
"""

# 다이나믹 프로그래밍 구현
x = int(input())
ans=[0 for _ in range(x+1)]

for i in range(2,x+1):
  ans[i]=ans[i-1]+1
  if i%2==0:
    ans[i]=min(ans[i],ans[i//2]+1)
  if i%3==0:
    ans[i]=min(ans[i],ans[i//3]+1)
  if i%5==0:
    ans[i]=min(ans[i],ans[i//5]+1)
print(ans[x])