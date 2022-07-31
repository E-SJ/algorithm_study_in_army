c,r = map(int,input().split())
shop_num = int(input())
mapp = [0 for _ in range(2*(c+r))]
shop_pos=[]
for i in range(shop_num):
  #shop_pos.append(list(map(int,input().split())))
  pos = list(map(int,input().split()))
  if pos[0]==1:
    shop_pos.append(c+c+r+r-pos[1])
  elif pos[0]==2:
    shop_pos.append(r+pos[1])
  elif pos[0]==3:
    shop_pos.append(pos[1])
  elif pos[0]==4:
    shop_pos.append(r+r+c-pos[1])
    
my_pos_list = list(map(int,input().split()))
if my_pos_list[0]==1:
  my_pos=c+c+r+r-my_pos_list[1]
elif my_pos_list[0]==2:
  my_pos=r+my_pos_list[1]
elif my_pos_list[0]==3:
  my_pos=my_pos_list[1]
elif my_pos_list[0]==4:
  my_pos=r+r+c-my_pos_list[1]

result=0
for i in range(len(shop_pos)):
  #print(min(abs(shop_pos[i]-my_pos),abs(shop_pos[i]-2*(c+r)-my_pos),abs(shop_pos[i]+2*(c+r)-my_pos)))
  result+= min(abs(shop_pos[i]-my_pos),abs(shop_pos[i]-2*(c+r)-my_pos),abs(shop_pos[i]+2*(c+r)-my_pos))

print(result)



