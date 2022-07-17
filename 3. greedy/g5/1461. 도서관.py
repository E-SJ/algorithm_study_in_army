import sys
input = sys.stdin.readline
n,m = map(int,input().split())
location = list(map(int,input().split()))
location.sort(key= lambda x:(abs(x)))

n_location = []
p_location = []
for item in location:
  if (item<0):
    n_location.append(item)
  else:
    p_location.append(item)
  


result=0
if (location[-1]>0) : #가장 먼거리에 있는 책이 양수위치일때
  if (len(n_location)>=1):
    if (len(n_location)<m): # 음수의 책 개수가 들수 있는 것보다 적을 때
      result+=abs(n_location[-1])*2
      for _ in range(len(n_location)):
        n_location.pop(0)
    else:
      if (len(n_location)%m>=1 and len(n_location)//m>=1): #음수 - 가까운거 먼저 처리
        result+=abs(n_location[len(n_location)%m-1])*2
        for _ in range(len(n_location)%m):
          n_location.pop(0)
      
      while len(n_location)!=0:  #음수 - 모두 처리
        result+=abs(n_location[m-1])*2
        for _ in range(m):
          n_location.pop(0)
  if (len(p_location)%m>=1 and len(p_location)//m>=1): #양수 - 가까운거 먼저 처리 #(and len(p_location)//m>=1)
    result+=p_location[len(p_location)%m-1]*2
    for _ in range(len(p_location)%m):
      p_location.pop(0)

  while len(p_location)>m: #양수 - 1회를 남기고 모두 처리
    result+=p_location[m-1]*2
    for _ in range(m):
      p_location.pop(0)

  if len(p_location)<=m: #양수 - 복귀할 필요 없는 거 처리
    result+=p_location[-1]

else:
  if (len(p_location)>=1):
    if (len(p_location)<m): # 양수의 책 개수가 들수 있는 것보다 적을 때
      result+=p_location[-1]*2
      for _ in range(len(p_location)):
        p_location.pop(0)
    else:
      if (len(p_location)%m>=1 and len(p_location)//m>=1): #양수 - 가까운거 먼저 처리
        result+=p_location[len(p_location)%m-1]*2
        for _ in range(len(p_location)%m):
          p_location.pop(0)
      
      while len(p_location)!=0:  #양수 - 모두 처리
        result+=p_location[m-1]*2
        for _ in range(m):
          p_location.pop(0)
  if (len(n_location)%m>=1 and len(n_location)//m>=1): #음수 - 가까운거 먼저 처리 #(and len(p_location)//m>=1)
    result+=abs(n_location[len(n_location)%m-1])*2
    for _ in range(len(n_location)%m):
      n_location.pop(0)

  while len(n_location)>m: #음수 - 1회를 남기고 모두 처리
    result+=abs(n_location[m-1])*2
    for _ in range(m):
      n_location.pop(0)

  if len(n_location)<=m: #음수 - 복귀할 필요 없는 거 처리
    result+=abs(n_location[-1])

print(result)
  
#아이디어: 먼 거리에 있는 책은 돌아올 필요가 없으므로 먼 거리의 책을 마지막에 두자!

#아이디어를 코드로 푸는 과정이 좀 어렵다. 예제 1번만 오답이 뜨니 그것만 고치자!
