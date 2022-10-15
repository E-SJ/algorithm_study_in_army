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
    cutcount=0
    temp=0
    minlength=l
    for i in range(len(cutlength)):
      temp+=cutlength[i]
      if (temp>=mid):
        minlength=min(temp,minlength)
        if (i!=len(cutlength)-1):
          temp=0
          cutcount+=1
    minlength=min(temp,minlength)
    print("trying",cutnum,left,mid,right,cutcount,minlength)
    if (cutcount>cutnum or minlength<mid):
      #ans=max(ans,minlength)
      left=mid+1
    elif (cutcount<cutnum or minlength<mid):
      right=mid-1
    else:
      ans=max(ans,minlength)
      right=mid-1
  print(ans)