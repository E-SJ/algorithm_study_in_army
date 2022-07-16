import sys
import heapq
n = int(input())
classes=[]

for i in range(n):
  heapq.heappush(classes,(list(map(int,sys.stdin.readline().split()))))


able_classes=[heapq.heappop(classes)[1]]

for _ in range(1,n):
  if able_classes[0]<=classes[0][0]:
    heapq.heappop(able_classes)
    heapq.heappush(able_classes,(heapq.heappop(classes)[1]))
  else:
    heapq.heappush(able_classes,(heapq.heappop(classes)[1]))
  #print(classes)
  #print(able_classes)
  
print(len(able_classes))

#아이디어 : heap 으로 시간 복잡도를 O(NlogN) 으로 줄이자!
#아이디어 : 이중 for문 없애자..
#해결 방법 : heap을 classes 와 able_classes 모두에 적용시켜 불필요한 루프를 제거! (classes는 강의가 먼저 시작되는 것([0]이 최소), 강의가 가장 먼저 끝나는 것([1]이 최소)만 확인하면 되므로 둘 다 minheap을 사용.)