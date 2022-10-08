import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
left = 0
right = N-1
l = 0
r = 0
_min = sys.maxsize
while left < right:
  _sum = arr[left] + arr[right]
  if abs(_sum) < _min:
    l = left
    r = right
    _min = abs(_sum)
  if _sum>0:
    right-=1
  elif _sum<0:
    left+=1
  else:
    break
print(arr[l], arr[r])