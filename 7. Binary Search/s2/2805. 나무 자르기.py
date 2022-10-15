n,m = map(int,input().split())
woods=list(map(int,input().split()))
woods.sort(reverse=True)
left=0
right=woods[0]
ans=0
while left<=right:
  mid=(left+right)//2
  #print("try",left,right,mid)
  temp=0
  for i in range(len(woods)):
    if (woods[i]>mid):
      temp+=woods[i]-mid
      if (temp>=m):
        ans=max(ans,mid)
        left=mid+1
        break
    else:
      right=mid-1
      break
  else:
    right=mid-1
print(ans)
  