""" # 이분탐색
import sys
input=sys.stdin.readline
r,c = map(int,input().split())
strings=[input() for _ in range(r)]
left = 1
right = r-1
ans=0
while left<=right:
  mid = (left+right)//2
  temp_list=[]
  for i in range(c):
    temp_str=""
    for j in range(mid,r):
      temp_str=temp_str+strings[j][i]
    if (temp_str in temp_list):
      right=mid-1
      break
    else:
      temp_list.append(temp_str)
  else:
    ans=max(ans,mid)
    left=mid+1
print(ans)
"""
#역순 정렬
import sys
input=sys.stdin.readline
r,c = map(int,input().split())
strings=["" for _ in range(c)]
for i in range(r):
  temp=input()
  for j in range(c):
    strings[j]=temp[j]+strings[j]
#print(strings)
ans=r-1
successiveflag=False
for i in range(0,r-1):
  temp=set()
  for j in range(0,c):
    temp.add(strings[j][i])
  #print(temp)
  if (len(temp)!=c):
    ans-=1
    if (successiveflag):
      print(ans)
      exit()
  else:
    successiveflag=True

print(ans)