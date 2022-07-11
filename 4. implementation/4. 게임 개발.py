v_size, h_size = map(int, input().split())
x,y,d = map(int, input().split())
mapp = []
forward_move=[(0,-1),(1,0),(0,1),(-1,0)]
back_move=[(0,1),(-1,0),(0,-1),(1,0)]
for i in range(v_size):
  mapp.append(list(map(int,input().split())))
  
breakflag=False
while 1:
  if (breakflag):
    break
  mapp[y][x]=2 # 2는 가본 칸
  count=0
  print(mapp)
  while 1:
    if count==4:
      x+=back_move[d][0]
      y+=back_move[d][1]
      if (mapp[y][x]==1):
        x+=forward_move[d][0]
        y+=forward_move[d][1]
        breakflag=True
        break
      else:
        count=0
    d=(d-1)%4
    x+=forward_move[d][0]
    y+=forward_move[d][1]
    if (mapp[y][x]!=0):
      x+=back_move[d][0]
      y+=back_move[d][1] 
      count+=1c
    else:
      break

result = 0
for line in mapp:
  for num in line:
    if num == 2:
      result+=1

print(result)