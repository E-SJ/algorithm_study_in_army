n,m = map(int,input().split())
matrix=[[0 for _ in range(m+1)]]
for _ in range(n):
  matrix.append([0]+list(map(int,input())))
dp=[[0 for _ in range(m+1)] for _ in range(n+1)]

result=0
for i in range(1,n+1):
  for j in range(1,m+1):
    if (i==1 or j==1):
      dp[i][j]=matrix[i][j]
    elif matrix[i][j]!=0:
      dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
    result=max(result,dp[i][j])
#print(*matrix,sep="\n")
#print(*dp,sep="\n")
print(result*result)
