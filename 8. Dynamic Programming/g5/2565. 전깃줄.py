import sys
input=sys.stdin.readline
n = int(input())
lines=[]
for _ in range(n):
  lines.append(tuple(map(int,input().split())))
lines.sort(key=lambda x:(x[0],x[1]))
lines.insert(0,tuple())
dp=[[] for _ in range(n+1)]
for i in range(1,n+1):
  dp[i]=dp[i-1].copy()
  for j in range(1,i):
    if (lines[i][0]>lines[j][0] and lines[i][1]<lines[j][1]):
      dp[i].append({i,j})


#print(*dp,sep="\n")
answer=0
while len(dp[-1]):
  freq=[0 for _ in range(101)]
  for cross in dp[-1]:
    cross=tuple(cross)  
    freq[cross[0]]+=1
    freq[cross[1]]+=1
  maxindex=freq.index(max(freq))
  dellist=[]
  for i in range(len(dp[-1])):
    if maxindex in dp[-1][i]:
      dellist.append(i)
  dellist.sort(reverse=True)
  for i in dellist:
    del dp[-1][i]
  answer+=1

print(answer)
      