import sys
input=sys.stdin.readline
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


while (len(chickens)>m):
  min_indexes=[]
  for item in popularity_chicken
    if item == min(popularity_chicken):
      min_indexes.append(item)
  for index in min_indexes:
    
  del chickens[min_index]
  
print(popularity_chicken)



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