n,m = map(int,input().split())
matrix=[[0 for _ in range(m+1)]]
for _ in range(n):
  matrix.append([0]+list(map(str,input())))
dp=[[0 for _ in range(m+1)] for _ in range(n+1)]


for step in range(1,max(n,m)+1):
  for i in range(step,m+1):
    if step>n or i>m:break
    if matrix[step][i]=='1':
      if (matrix[step-1][i-1]==matrix[step][i-1]==matrix[step-1][i]=='1' and dp[step-1][i-1]==dp[step][i-1]==dp[step-1][i]):
        dp[step][i]=dp[step-1][i-1]+1
    else:dp[step][i]=max(dp[step-1][i-1],dp[step][i-1],dp[step-1][i],dp[step][i],int(matrix[step][i]))
  for i in range(step,n+1):
    if step>m or i>n:break
    if matrix[i][step]=='1':
      if (matrix[i-1][step-1]==matrix[i][step-1]==matrix[i-1][step]=='1' and dp[i-1][step-1]==dp[i][step-1]==dp[i-1][step]):
        dp[i][step]=dp[i-1][step-1]+1
    else: dp[i][step]=max(dp[i-1][step-1],dp[i][step-1],dp[i-1][step],dp[i][step],int(matrix[i][step]))
      
#print(*matrix,sep="\n")
print(*dp,sep="\n")
print(dp[n][m]*dp[n][m])
