import sys
input = sys.stdin.readline
import heapq
n = int(input())

classes = []
for i in range(n):
  heapq.heappush(classes,list(map(int,input().split()))[1:])

able_classes = []
heapq.heappush(able_classes,heapq.heappop(classes)[1])
for i in range(n-1):
  if (classes[0][0]<able_classes[0]):
    heapq.heappush(able_classes,heapq.heappop(classes)[1])
    
  else:
    heapq.heappop(able_classes)
    heapq.heappush(able_classes, heapq.heappop(classes)[1])

print(len(able_classes))

#아이디어: 11000과 동일하다! 근데 왜 오랫동안 붙들었을까..