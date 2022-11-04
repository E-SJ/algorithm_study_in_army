from bisect import bisect_left, bisect_right

n = int(input())
arr = list(map(int,input().split()))
dp=[0]*(n+1)
lis=[arr[0]]
#len_lis=1
for i in range(1,n):
  if lis[-1]<arr[i]:
    lis.append(arr[i])
  else:
    index=bisect_left(lis,arr[i])
    lis[index]=arr[i]
  #print(*lis)


print(len(lis))
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