n,k = map(int,input().split())
coins=[]
for i in range(n):
  coins.append(int(input()))
coins.sort(reverse=True)
result=0
for coin in coins:
  num=(k//coin)
  result+=num
  k-=num*coin
print(result)