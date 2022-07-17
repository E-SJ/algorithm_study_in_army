n = int(input())
ballons = list(map(int,input().split()))

arrow=[0 for _ in range(1000001)]
result=0
for i in range(n):
  if (arrow[ballons[i]]<=0):
    arrow[ballons[i]-1]+=1
    result+=1
  else:
    arrow[ballons[i]]-=1
    arrow[ballons[i]-1]+=1

print(result)


#알고리즘 자체는 잘 동작하는데.. 시간복잡도를 어떻게 낮출 수 있을까?

#아이디어: 화살을 한번 쏘고, 그 이후를 하나하나 계산하는 것이 아니라, 화살을 연속해서 쏘면서 각 풍선에 대해 계산을 해나가자..!