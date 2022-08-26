import sys
input=sys.stdin.readline
n=int(input())
flowers=[]
for _ in range(n):
  sm,sd,em,ed = map(int,input().split())
  flowers.append((sm,sd,em,ed))
flowers.sort(key=lambda x:(x[0],x[1],x[2],x[3]))

#print(*flowers)
#exit()
count=0
mon_max,day_max=flowers[0][2],flowers[0][3]
mon_max_temp,day_max_temp=-1,-1
successflag=False
_3_1_flag=False
for i in range(n):
  if (mon_max>=12 and _3_1_flag):
    successflag=True
    break
  if (flowers[i][0]>mon_max or (flowers[i][0]==mon_max and flowers[i][1]>day_max)):
    print(0)
    exit()
  if (flowers[i][0]==1 or flowers[i][0]==2 or (flowers[i][0]==3 and flowers[i][1]==1)): #3월 1일 부터만 체크하면 되므로
    _3_1_flag=True
    if (flowers[i][2]>mon_max): #3월 1일 전에 피는 꽂들 중 가장 늦게 지는 시기를 고른다.
      mon_max=flowers[i][2]
      day_max=flowers[i][3]
      #print(mon_max,day_max,count)
    elif (flowers[i][2]==mon_max and flowers[i][3]>day_max):
      day_max=flowers[i][3]
      #print(mon_max,day_max,count)
  else:
    if (_3_1_flag==False):
      print(0)
      exit()
    if (flowers[i][2]>=12):
      successflag=True
    if (flowers[i][0]<mon_max or (flowers[i][0]==mon_max and flowers[i][1]<=day_max)):
      if (flowers[i][2]>mon_max_temp):
        mon_max_temp = flowers[i][2]
        day_max_temp = flowers[i][3]
      elif (flowers[i][2]==mon_max_temp and flowers[i][3]>day_max_temp):
        day_max_temp = flowers[i][3]
        
      if (i+1<n and (flowers[i+1][0]<mon_max or (flowers[i+1][0]==mon_max and flowers[i+1][1]<=day_max))):
        continue
      else:
        mon_max=mon_max_temp
        day_max=day_max_temp
        mon_max_temp,day_max_temp=-1,-1
        count+=1 
        #print(mon_max,day_max,count)
        if (mon_max>=12):
          successflag=True
if (successflag):
  print(count+1)
else:
  print(0)
    