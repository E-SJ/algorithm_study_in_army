n = int(input())
arr = list(map(int,input().split()))
point1=0
point2=n-1
ans = 200000000
while point1!=point2:
  temp = arr[point1]+arr[point2]
  if (temp==0):
    print(0)
    exit()
  elif (temp>0):
    if (abs(temp)<abs(ans)):
      ans = temp
    point2-=1
  elif (temp<0):
    if (abs(temp)<abs(ans)):
      ans = temp
    point1+=1

print(ans)
