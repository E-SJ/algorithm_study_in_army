import sys
input = sys.stdin.readline
dp=[[[1 for _ in range(21)]for _ in range(21)]for _ in range(21)]

for i in range(1,21):
  for j in range(1,21):
    for k in range(1,21):
      if i < j and j < k:
        dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
      elif i>0 and j>0 and k>0:
        dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]
        
def w(a,b,c):
  if a <= 0 or b <= 0 or c <= 0:
    return 1

  elif a > 20 or b > 20 or c > 20:
    return dp[20][20][20]

  else:
    return dp[a][b][c]

a,b,c = map(int,input().split())
while not (a==-1 and b==-1 and c==-1):
  print(f"w({a}, {b}, {c}) =",w(a,b,c))
  a,b,c = map(int,input().split())