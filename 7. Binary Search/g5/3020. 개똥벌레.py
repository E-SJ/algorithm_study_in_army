from bisect import bisect_left,bisect_right
import sys
input=sys.stdin.readline
n,h = map(int,input().split())
s=[] #석순
z=[] #종유석
for i in range(n):
  temp=int(input())
  if (i%2==0): #석순
    s.append(temp)
  else: #종유석
    z.append(temp)

s.sort()
z.sort()

def binary_search(arr,value):
  start=0
  end=len(arr)-1
  mid=(end+start)//2
  while start<=end:
    if arr[mid]==value:
      return mid
    elif arr[mid]>value:
      end=mid-1
      mid=(end+start)//2
    elif arr[mid]<value:
      start=mid+1
      mid=(end+start)//2
  return -1

obs=200000
count=0
for sector in range(h):
  result = (len(s)-bisect_right(s,sector)) + (len(z)-bisect_right(z,h-1-sector))

  if (result<obs):
    obs=result
    count=1
  elif (result==obs):
    count+=1


print(obs, count)