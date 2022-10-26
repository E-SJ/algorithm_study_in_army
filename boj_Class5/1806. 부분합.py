n,s = map(int,input().split())
arr=[0]+list(map(int,input().split()))
dp=[0]*(n+1)
startindex=0
endindex=-1
result=n+1
for i in range(1,n+1):
  #print("result",result)
  dp_temp=dp[i-1]+arr[i]
  if (dp[i-1]+arr[i]<s):
    dp[i]=dp_temp
  else:
    endindex=i
    temp=dp_temp-arr[startindex]
    while temp>=s:
      dp_temp=temp
      startindex+=1
      temp-=arr[startindex]
    #print(endindex,startindex)
    result=min(result,endindex-startindex+1)
    dp[i]=dp_temp
#print(arr)
#print(dp)
#print(result)
if (endindex==-1):
  print(0)
else:
  print(result)