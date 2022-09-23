code = input()
dp=[0 for _ in range(len(code))]
if (code[0]!='0'):
  dp[0]=1
else:
  print(0)
  exit()
for i in range(1,len(code)):
  if (code[i]=='0'):
    if (code[i-1]!='1' and code[i-1]!='2'):
      print(0)
      exit()
  else:
    dp[i]=dp[i-1]
  if (code[i-1]=='1'):
    if (i-2>=0):
      dp[i]+=dp[i-2]
    else:
      dp[i]+=1
  elif (code[i-1]=='2'):
    if (code[i]=='0' or code[i]=='1' or code[i]=='2' or code[i]=='3' or code[i]=='4' or code[i]=='5' or code[i]=='6'):
      if (i-2>=0):
        dp[i]+=dp[i-2]
      else:
        dp[i]+=1
  

print(dp[-1]%1000000)