n,k = map(int,input().split())
if (n%2==0): #짝수
  left=0
  right=n//2
  while left<=right:
    mid=(left+right)//2
    if ((n+2)//2-mid)*((n+2)//2+mid)>k:
      left=mid+1
    elif ((n+2)//2-mid)*((n+2)//2+mid)<k:
      right=mid-1
    else:
      print("YES")
      exit()
else: #홀수
  left=0
  right=n//2
  while left<=right:
    mid=(left+right)//2
    if ((n+2)//2-mid)*((n+2)//2+1+mid)>k:
      left=mid+1
    elif ((n+2)//2-mid)*((n+2)//2+1+mid)<k:
      right=mid-1
    else:
      print("YES")
      exit()
      
print("NO")
