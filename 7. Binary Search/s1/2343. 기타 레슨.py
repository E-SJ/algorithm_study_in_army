n,m = map(int,input().split())
length=list(map(int,input().split()))
left=0
right=n*max(length)
ans=right
while left<=right:
  mid = (left+right)//2
  #print("try",mid)
  sum=0
  count=1
  for i in range(len(length)):
    sum+=length[i]
    if (sum>mid):
      sum=length[i]
      count+=1
      if (sum>mid) or (count>m):
        left=mid+1
        break
  else:
    ans=min(ans,mid)
    right=mid-1

print(ans)