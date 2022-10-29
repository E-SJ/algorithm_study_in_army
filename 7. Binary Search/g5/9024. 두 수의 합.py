from bisect import bisect_left,bisect_right
import sys
input=sys.stdin.readline
t = int(input())
for _ in range(t):
  n,k = map(int,input().split())
  arr = list(map(int,input().split()))
  val = 10**9
  ans=1
  arr.sort()
  closest, closestCount = 10**9, 0
  for i in range(len(arr)):
    left, right = i + 1, len(arr) - 1
    while left <= right:
      mid = left + (right - left) // 2
      _sum = arr[i] + arr[mid]
      if abs(k - _sum) < closest:
        closest = abs(k - _sum)
        closestCount = 1
      elif abs(k - _sum) == closest:
        closestCount += 1
      if _sum > k:
        right = mid - 1
      else:
        left = mid + 1
  print(closestCount)
