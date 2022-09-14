n=int(input())
boxes=list(map(int,input().split()))
boxes.insert(0,0)
dp=[0 for i in range(n+1)]
dp[0]=0
dp[1]=1
for i in range(2,n+1):
  index=0
  for j in range(0,i):
    if dp[index]<=dp[j] and boxes[j]<boxes[i]:
      index=j
  dp[i]=dp[index]+1

print(max(dp))