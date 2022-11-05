import sys
from copy import copy
from bisect import bisect_left as bl
input=sys.stdin.readline

n = int(input())
pos=[-1] * 500001
pole_A=[]
for _ in range(n):
  a,b = map(int,input().split())
  pos[a]=b
  pole_A.append(a)
pole_A.sort()
lis = [pos[pole_A[0]]]
rec = [0]
for i in pole_A[1:]:
  if lis[-1]<pos[i]:
    lis.append(pos[i])
    rec.append(len(lis)-1)
  else:
    index=bl(lis,pos[i])
    lis[index]=pos[i]
    rec.append(index)
#print(lis)

temp = max(rec)
not_ans=[]

for i in range(len(rec)-1,-1,-1):
  if temp==-1:
    break
  if rec[i]==temp:
    temp-=1
    not_ans.append(pole_A[i])

ans=copy(pole_A)
for i in not_ans:
  ans.remove(i)
print(n-len(lis))
print(*ans,sep='\n')
    