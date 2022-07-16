n = int(input()) # 크레인 개수
weight_limit=list(map(int,input().split())) # 각 크레인 무게 제한
m = int(input()) # 박스 개수
box_weight = list(map(int,input().split())) #각 박스 무게
weight_limit.sort(reverse=True)
box_weight.sort(reverse=True)
crane_use=[0 for _ in range(n)]
#boxtransfered=[0 for _ in range(m)]

t=0
while 1:
  for crane in range(n):
    for box in range(m):
      if (weight_limit[crane]>=box_weight[box]):
        #crane_use[crane]=1
        box_weight.remove(box_weight[box])
        m-=1
        break

  t+=1
  crane_use=[0 for _ in range(n)]
  if (m==0):
    break

print(t)

# 알고리즘 자체는 정상적으로 답을 도출하지만, 시간 복잡도가 너무 높다. 시간 복잡도를 낮춰보자.

    
      
      
      
      