n=int(input())
from collections import deque
import time
table=[[] for _ in range(n+1)]
t=time.time()
q=deque()
q.append(1)
table[1]=[1]
while q:
  for _ in range(len(q)):
    num=q.popleft()
    if (num*3<n+1 and table[num*3]==[]):
      table[num*3]=table[num]+[num*3]
      q.append(num*3)
    if (num*2<n+1 and table[num*2]==[]):
      table[num*2]=table[num]+[num*2]
      q.append(num*2)
    if (num+1<n+1 and table[num+1]==[]):
      table[num+1]=table[num]+[num+1]
      q.append(num+1)
#print(t-time.time())
print(len(table[n])-1)
print(*table[n][::-1],sep=" ")