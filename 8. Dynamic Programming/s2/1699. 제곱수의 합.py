n = int(input())
dp=[0 for _ in range(n+1)]
sqrts=[i*i for i in range(int(n**0.5)+2)]
def lowersqrts(num):
  result=sqrts[1:int(i**(0.5))+1]
  return result

for i in range(1,n+1):
  minnum=999999999999999
  for sqr in lowersqrts(i):
    minnum=min(minnum,dp[i-sqr])
  dp[i]=minnum+1
    
      
      
print(dp[-1])