import sys
input = sys.stdin.readline

n = int(input()) # 크레인 개수
weight_limit=list(map(int,input().split())) # 각 크레인 무게 제한
m = int(input()) # 박스 개수
box_weight = list(map(int,input().split())) #각 박스 무게
weight_limit.sort(reverse=True)
box_weight.sort(reverse=True)
#crane_use=[0 for _ in range(n)]
#boxtransfered=[0 for _ in range(m)]

if (weight_limit[0]<box_weight[0]):
  print('-1')
  exit()

t=0
while True:
  for crane in range(n):
    if (m==0):
      break
    if weight_limit[crane]<box_weight[-1]:
      break
    for box in range(m):
      if (weight_limit[crane]>=box_weight[box]):
        #crane_use[crane]=1
        del box_weight[box]
        m-=1
        break

  t+=1
  if (m==0):
    break
  #crane_use=[0 for _ in range(n)]
  

print(t)

# 알고리즘 자체는 정상적으로 답을 도출하지만, 시간 복잡도가 너무 높다. 시간 복잡도를 낮춰보자.
# 22~23 줄 코드가 핵심! 남은 박스중에서 가장 가벼운 박스가 현재 크레인의 무게 제한보다 크다면 바로 나머지 크레인도 버리기! (다음 반복될 크레인은 당연히 현재 크레인 무게제한보다 더 낮은 무게일 것이므로..)

    
      
      
      
      