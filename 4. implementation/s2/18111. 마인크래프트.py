import sys
input = sys.stdin.readline
n,m,b = map(int,input().split())

mapp=[]
for _ in range(n):
  mapp.append(list(map(int,input().split())))
answers=[]
for height in range(257):
  answer=0
  blocks=0
  for i in range(n):
    for j in range(m):
      if (height>mapp[i][j]):
        answer+=(height-mapp[i][j])*1
        blocks-=1
      elif (height<mapp[i][j]):
        answer+=(mapp[i][j]-height)*2
        blocks+=1