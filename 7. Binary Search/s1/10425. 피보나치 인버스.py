from bisect import bisect_right
import sys
input=sys.stdin.readline
fib=[0]*100001
fib[0]=0
fib[1]=1
for i in range(2,100001):
  fib[i]=fib[i-2]+fib[i-1]
n=int(input())
for _ in range(n):
  num = int(input())
  print(bisect_right(fib,num)-1)