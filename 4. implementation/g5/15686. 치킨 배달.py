import sys
input=sys.stdin.readline
import time
n, m = map(int,input().split())
mapp=[]
for _ in range(n):
  mapp.append(list(map(int,input().split())))
chickens=[]
houses=[]
for i in range(n):
  for j in range(n):
    if (mapp[i][j]==2):
      chickens.append([i,j])
    elif(mapp[i][j]==1):
      houses.append([i,j])
popularity_chicken=[0 for _ in range(len(chickens))]



for i in range(len(houses)):
  min_distance=abs(chickens[0][0]-houses[i][0])+abs(chickens[0][1]-houses[i][1])
  nearest_chicken=chickens[0]
  for j in range(len(chickens)):
    if (min_distance>abs(chickens[j][0]-houses[i][0])+abs(chickens[j][1]-houses[i][1])):
      min_distance=abs(chickens[j][0]-houses[i][0])+abs(chickens[j][1]-houses[i][1])
      nearest_chicken=chickens[j]
  popularity_chicken[chickens.index(nearest_chicken)]+=1


def cal_distances():
  distances_chickens=[]
  for i in range(len(houses)):
    min_distance=abs(chickens[0][0]-houses[i][0])+abs(chickens[0][1]-houses[i][1])
    nearest_chicken=chickens[0]
    for j in range(len(chickens)):
      if (min_distance>abs(chickens[j][0]-houses[i][0])+abs(chickens[j][1]-houses[i][1])):
        nearest_chicken=chickens[j]
        min_distance=abs(chickens[j][0]-houses[i][0])+abs(chickens[j][1]-houses[i][1])
    distances_chickens.append(abs(nearest_chicken[0]-houses[i][0])+abs(nearest_chicken[1]-houses[i][1]))
    return distances_chickens


distances_chickens=[]
for i in range(len(houses)):
  min_distance=abs(chickens[0][0]-houses[i][0])+abs(chickens[0][1]-houses[i][1])
  nearest_chicken=chickens[0]
  for j in range(len(chickens)):
    if (min_distance>abs(chickens[j][0]-houses[i][0])+abs(chickens[j][1]-houses[i][1])):
      nearest_chicken=chickens[j]
      min_distance=abs(chickens[j][0]-houses[i][0])+abs(chickens[j][1]-houses[i][1])
  distances_chickens.append(abs(nearest_chicken[0]-houses[i][0])+abs(nearest_chicken[1]-houses[i][1]))




while (len(chickens)>m):
  min_indexes = [i for i, ele in enumerate(popularity_chicken) if ele == min(popularity_chicken)]
  if (len(min_indexes)==1):
    mapp[chickens[min_indexes[0]][0]][chickens[min_indexes[0]][1]]=0
    del chickens[min_index]
  else:
    distances=[]
    for a in range(len(min_indexes)):
      backup=chickens[a].copy()
      del chickens[a]
      
      distances_chickens=[]
      for i in range(len(houses)):
        min_distance=abs(chickens[0][0]-houses[i][0])+abs(chickens[0][1]-houses[i][1])
        nearest_chicken=chickens[0]
        for j in range(len(chickens)):
          if (min_distance>abs(chickens[j][0]-houses[i][0])+abs(chickens[j][1]-houses[i][1])):
            nearest_chicken=chickens[j]
            min_distance=abs(chickens[j][0]-houses[i][0])+abs(chickens[j][1]-houses[i][1])
        distances_chickens.append(abs(nearest_chicken[0]-houses[i][0])+abs(nearest_chicken[1]-houses[i][1]))

      chickens.insert(i,backup)
      distances.append(sum(distances_chickens))
    min_index = distances.index(min(distances))
    del chickens[min_index]
    #del min_indexes[min_indexes.index(min_index)]
    mapp[chickens[min_indexes[min_indexes.index(min_index)]][0]][chickens[min_indexes[min_indexes.index(min_index)]][1]]=0
    print(chickens)
    
    #print(distances)
    #print(distances.index(min(distances)))
  

distances_chickens=[]
for i in range(len(houses)):
  min_distance=abs(chickens[0][0]-houses[i][0])+abs(chickens[0][1]-houses[i][1])
  nearest_chicken=chickens[0]
  for j in range(len(chickens)):
    if (min_distance>abs(chickens[j][0]-houses[i][0])+abs(chickens[j][1]-houses[i][1])):
      nearest_chicken=chickens[j]
      min_distance=abs(chickens[j][0]-houses[i][0])+abs(chickens[j][1]-houses[i][1])
  distances_chickens.append(abs(nearest_chicken[0]-houses[i][0])+abs(nearest_chicken[1]-houses[i][1]))
  
print(chickens)
print(distances_chickens) 

result = 0
for i in range(len(distances_chickens)):
  result+=distances_chickens[i]
print(result)