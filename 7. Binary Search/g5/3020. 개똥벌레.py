import sys
input=sys.stdin.readline
n,h = map(int,input().split())
s=[] #석순
z=[] #종유석
for i in range(n):
  temp=int(input())
  if (i%2==0): #석순
    s.append(int(input()))
  else: #종유석
    z.append(int(input()))

s.sort()
z.sort()
#시간초과 예상