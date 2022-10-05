import sys
input=sys.stdin.readline
n,k = map(int,input().split())
level=[int(input()) for _ in range(n)]
left=0
right=2000000001
answer=0
while left<=right:
  mid = (left+right)//2
  temp=k
  for i in range(n):
    if mid>level[i]:
      temp-=(mid-level[i])
  if temp<0:
    right=mid-1
  else:
    left=mid+1
    answer=max(mid,answer)
print(answer)