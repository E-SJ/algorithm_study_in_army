import sys
input = sys.stdin.readline
n,m,b = map(int,input().split())

mapp=[]
for _ in range(n):
  mapp.append(list(map(int,input().split())))
answers=[]
for height in range(256):
  answer=0
  blocks=b
  for i in range(n):
    for j in range(m):
      ground=mapp[i][j]
      if (height>ground):
        answer+=(height-ground)
        blocks-=1
      elif (height<ground):
        answer+=(ground-height)*2
        blocks+=1
      #if (blocks<0):
      #  break
    #if (blocks<0):
    #    break
  if (blocks>=0):
    answers.append([answer,height])

answers.sort(key=lambda x:(x[0],x[1]))
#print(answers)
print(answers[0][0],answers[0][1],end="")