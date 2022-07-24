from itertools import permutations
n = int(input())
people = list(map(int,input().split()))
test=[i for i in range(1,n+1)]
answer=()
for tocheck in permutations(test):
  breakflag=False
  for i in range(n): #키가 작은 사람부터 확인
    count=0
    for j in range(tocheck.index(i+1)-1,-1,-1):
      if (tocheck[j]>i+1):
        count+=1
    if (count!=people[i]):
      breakflag=True
      break
  if (breakflag):
    continue
  answer=tocheck

for item in answer:
  print(item,end=" ")

