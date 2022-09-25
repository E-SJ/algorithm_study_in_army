str1='0'+input()
str2='0'+input()
dp=[[0 for _ in range(len(str2))] for _ in range(len(str1))]
for i in range(1,len(str1)):
  for j in range(1,len(str2)):
    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    if (str1[i]==str2[j]):
      dp[i][j]=max(dp[i][j],dp[i-1][j-1]+1)

ans=""
y=len(str1)-1
x=len(str2)-1
for _ in range(dp[-1][-1],0,-1):
  while True:
    if (dp[y][x]==dp[y-1][x]):
      y-=1
    elif (dp[y][x]==dp[y][x-1]):
      x-=1
    else:
      ans=str1[y]+ans
      y-=1
      x-=1
      break
print(dp[-1][-1])
print(ans)