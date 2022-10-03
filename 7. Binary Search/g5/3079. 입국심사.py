import sys
input=sys.stdin.readline
n,m = map(int,input().split())
T=[int(input()) for _ in range(n)]
T.sort()

left=0
right=T[-1]*m
answer=T[-1]*m
while left<=right:
  mid = (left+right)//2
  people=0
  for i in range(len(T)):
    people+=mid//T[i]
  if (people>=m):
    right=mid-1
    answer=min(answer,mid)
  elif (people<m):
    left=mid+1
print(answer)
