n=int(input())
humans=list(map(int,input().split()))
humans.sort()
result=0
for i in range(n):
  result+=(humans[i])*(n-i)
print(result)