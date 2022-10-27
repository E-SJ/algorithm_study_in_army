import sys
from itertools import combinations
input=sys.stdin.readline
while True:
  arr=list(map(int,input().split()))
  if (arr==[0]):
    break
  arr=arr[1:]
  for i in combinations(arr,6):
    print(*i)
  print("")