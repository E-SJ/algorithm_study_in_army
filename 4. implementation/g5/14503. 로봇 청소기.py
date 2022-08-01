n,m = map(int,input().split())
pos_y , pos_x , d = map(int,input().split())
mapp=[]
d_for=[(-1,0),(0,1),(1,0),(0,-1)]
d_back=[(1,0),(0,-1),(-1,0),(0,1)]
for _ in range(n):
  mapp.append(list(map(int,input().split())))


count=0
while True:
  if (mapp[pos_y][pos_x]==0):
    count+=1
  mapp[pos_y][pos_x]=2
  d=(d-1)%4
  if (mapp[pos_y+d_for[d][0]][pos_x+d_for[d][1]]==0):
    pos_y+=d_for[d][0]
    pos_x+=d_for[d][1]
    continue
  else:
    moveflag=False
    for _ in range(3):
      d=(d-1)%4
      if (mapp[pos_y+d_for[d][0]][pos_x+d_for[d][1]]==0):
        pos_y+=d_for[d][0]
        pos_x+=d_for[d][1]
        moveflag=True
        break
    if (moveflag):
      continue
    else:
      if (mapp[pos_y+d_back[d][0]][pos_x+d_back[d][1]]!=1):
        pos_y+=d_back[d][0]
        pos_x+=d_back[d][1]
        continue
      else:
        break
        
print(count)