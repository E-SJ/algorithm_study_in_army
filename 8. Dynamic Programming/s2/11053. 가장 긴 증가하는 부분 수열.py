n = int(input())
series=list(map(int,input().split()))
max=-1
length=0
for i in range(0,n):
  if (max<series[i]):
    max=series[i]
    length+=1
print(length)


