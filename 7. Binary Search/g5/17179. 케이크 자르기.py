import bisect
import sys
input=sys.stdin.readline
n,m,l = map(int,input().split())
cutpoints=[int(input()) for _ in range(m)]

cutlength=[cutpoints[0]] # m+1개
for i in range(1,m):
  cutlength.append(cutpoints[i]-cutpoints[i-1])
cutlength.append(l-cutpoints[m-1])

cutnums=[int(input()) for _ in range(n)]
for cutnum in cutnums:
  left=1
  right=l
  ans=0
  while left<=right:
    mid = (left+right)//2 #자른 빵의 최소 길이
    cutcount=-1
    temp=0
    for i in range(len(cutlength)):
      temp+=cutlength[i]
      if (temp>=mid):
        temp=0
        cutcount+=1
    #print("trying",cutnum,left,mid,right,cutcount)
    if (cutcount>cutnum):
      ans=max(ans,mid)
      left=mid+1
    elif (cutcount<cutnum):
      right=mid-1
    else:
      ans=max(ans,mid)
      left=mid+1
  print(ans)