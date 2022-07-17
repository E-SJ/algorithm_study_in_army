n = int(input())
heights=list(map(int,input().split()))

sum = 0
for item in heights:
  sum+=item
if (sum%3!=0):
  print("NO")
else:
  count=0
  for i in range(n):
    count+=heights[i]//2
  if (count>=sum//3):
    print("YES")
  else:
    print("NO")
    
#아이디어를 생각하기가 어려운 문제이다.
#참고: https://xkdlaldfjtnl.tistory.com/66
#1과 2가 아닌 2와 3 등 어려운 경우도 생각해보는 것도 나중에 도움이 될 듯.