import sys
input=sys.stdin.readline
n,c = map(int,input().split())
houses=[int(input()) for _ in range(n)]
houses.sort()
dist=[]
for i in range(1,n):
  dist.append(houses[i]-houses[i-1])
#print(houses)
#print(dist)
start=0
end=1000000000
ans=start
while (start<=end):
  mid = (start+end)//2
  #print(start,mid,end,ans)
  temp=0
  count=1
  for i in range(n-1):
    temp+=dist[i]
    if (temp>=mid):
      temp=0
      count+=1
  if (count>=c):
    ans=max(ans,mid)
    start=mid+1
  else:
    end=mid-1
    

print(ans)