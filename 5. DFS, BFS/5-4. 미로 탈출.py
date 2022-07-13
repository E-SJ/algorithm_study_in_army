from collections import deque
import time
n,m = map(int,input().split())

graph = []
for i in range(n):
  graph.append(list(map(int,input())))

queue=deque()
queue.append((0,0))

count=0
breakflag=False
while not breakflag:
  count+=1
  for _ in range(len(queue)):
    y,x=queue[0]
    queue.popleft()
    if graph[y][x]!=1:
      continue
    if (y,x)==(n-1,m-1):
      breakflag=True
      break
    if (y<n-1):
      graph[y][x]=0 # 방문 표시는 큐에서 꺼낼때가 아니라 큐에 넣을때!!!
      queue.append((y+1,x))
    if (y>0):
      graph[y][x]=0 # 그래야 불필요한 큐에서 각각 방문표시를 하지 않고,
      queue.append((y-1,x))
    if (x<m-1):
      graph[y][x]=0 # 빠르게 해당 큐를 끝낼 수 있음
      queue.append((y,x+1))
    if (x>0):
      graph[y][x]=0
      queue.append((y,x-1))

print(count)

# 백준 참고: https://www.acmicpc.net/problem/2178

#복잡도를 낮추려면(중요): 
# 1. dequeue를 착실히 하여 queue에 불필요한 데이터가 쌓이지 않도록 주의 (넘어가는 상황 전에 dequeue가 될 수 있도록 앞에다 둬야함) -> 그렇지 않으면 시간 증가 + 메모리 증가
# 2. graph에 방문 표시 할 때 불필요한 큐가 일일이 중복된 방문 표시를 하지 않도록 주의


""" 느린 코드
from collections import deque
import time
n,m = map(int,input().split())

graph = []
for i in range(n):
  graph.append(list(map(int,input())))

queue=deque()
queue.append((0,0))

count=0
breakflag=False
while not breakflag:
  count+=1
  for y,x in list(queue):
    if graph[y][x]!=1:
      continue
    if (y,x)==(n-1,m-1):
      breakflag=True
      break
    queue.popleft()
    if (y<n-1):
      graph[y][x]=0 # 방문 표시를 하여 루프 제거
      queue.append((y+1,x))
    if (y>0):
      graph[y][x]=0 # 방문 표시를 하여 루프 제거
      queue.append((y-1,x))
    if (x<m-1):
      graph[y][x]=0 # 방문 표시를 하여 루프 제거
      queue.append((y,x+1))
    if (x>0):
      graph[y][x]=0 # 방문 표시를 하여 루프 제거
      queue.append((y,x-1))

print(count)
"""
