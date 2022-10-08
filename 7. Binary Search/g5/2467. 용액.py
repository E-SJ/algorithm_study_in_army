n=int(input())
arr=list(map(int,input().split()))
arr.sort()
ans=2000000001
ans_tuple=tuple()
p1=0
p2=n-1
while p1<p2:
  value=arr[p1]+arr[p2]
  if (ans>abs(value)):
    ans=abs(value)
    ans_tuple=(arr[p1],arr[p2])
  if value<0:
    p1+=1
  elif value>0:
    p2-=1
  else:
    print(arr[p1],arr[p2])
    exit()
print(*ans_tuple)