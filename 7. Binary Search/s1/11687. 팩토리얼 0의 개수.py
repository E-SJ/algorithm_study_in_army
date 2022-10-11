n = int(input())
start=0
end=5000000000
ans=end
ansflag=False
while start<=end:
  mid=(start+end)//2
  #print(start,mid,end)
  count=0
  mul5=5
  while mid>=mul5:
    count+=mid//mul5
    mul5*=5
  if (count>n):
    end=mid-1
  elif (count<n):
    start=mid+1
  else:
    ansflag=True
    ans=min(ans,mid)
    end=mid-1

if (not ansflag):
  print(-1)
else:
  print(ans)
