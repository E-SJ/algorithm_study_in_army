import sys
import heapq
n = int(input())
classes=[]

for i in range(n):
  heapq.heappush(classes,(list(map(int,sys.stdin.readline().split()))))


able_classes=[heapq.heappop(classes)]

for _ in range(1,n):
  for j in range(len(able_classes)):
    if able_classes[j][1]<=classes[0][0]:
      able_classes[j][1]=classes[0][1]
      break
    else:
      if (j == len(able_classes)-1):
        able_classes.append(heapq.heappop(classes))
        
        break

print(len(able_classes))

#아이디어 : heap 으로 시간 복잡도를 O(NlogN) 으로 줄이자!
#아이디어 : 이중 for문 없애자..