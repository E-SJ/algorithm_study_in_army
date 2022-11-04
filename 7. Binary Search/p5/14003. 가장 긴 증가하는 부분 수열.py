from bisect import bisect_left, bisect_right

n = int(input())
arr = list(map(int,input().split()))
dp=[0]*(n+1)
lis=[arr[0]]
rec=[0]
#len_lis=1
for i in range(1,n):
  if lis[-1]<arr[i]:
    lis.append(arr[i])
    rec.append(len(lis)-1)
  else:
    index=bisect_left(lis,arr[i])
    lis[index]=arr[i]
    rec.append(index)
  #print(*lis)

temp=max(rec)
ans=[]
for i in range(n-1,-1,-1):
  if rec[i]==temp:
    ans.append(arr[i])
    temp-=1
#print(lis)
#print(rec)
print(len(lis))
print(*ans[::-1])
#print(*lis)
"""
print(max(dp))
max_dp=max(dp)
ans=[]
for i in range(n,0,-1):
  if dp[i]==max_dp:
    ans.insert(0,arr[i])
    max_dp-=1
    continue
print(*ans)
"""  