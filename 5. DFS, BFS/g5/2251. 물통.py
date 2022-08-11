from collections import deque
A,B,C = map(int,input().split())
Q=deque()
visited=[]
def bfs():
  Q.append([0,0,C])
  visited.append([0,0,C])
  while (len(Q)):
    for _ in range(len(Q)):
      item = Q.popleft()
      #print(item)
      AB = abs(item[0]-item[1])
      BC = abs(item[1]-item[2])
      AC = abs(item[2]-item[0])
      if (item[0]>0 and item[1]<B):
        water=max(min(item[0],B-item[1]),0)
        node=[item[0]-water,item[1]+water,item[2]]
        if not (node in visited):
          Q.append(node)
          visited.append(node)
      if (item[0]>0 and item[2]<C):
        water=max(min(item[0],C-item[2]),0)    
        node=[item[0]-water,item[1],item[2]+water]
        if not (node in visited):
          Q.append(node)
          visited.append(node)
      if (item[1]>0 and item[0]<A):
        water=max(min(item[1],A-item[0]),0)     
        node=[item[0]+water,item[1]-water,item[2]]
        if not (node in visited):
          Q.append(node)
          visited.append(node)
      if (item[1]>0 and item[2]<C):
        water=max(min(item[1],C-item[2]),0)    
        node=[item[0],item[1]-water,item[2]+water]
        if not (node in visited):
          Q.append(node)
          visited.append(node)
        
      if (item[2]>0 and item[0]<A):
        water=max(min(item[2],A-item[0]),0)       
        node=[item[0]+water,item[1],item[2]-water]
        if not (node in visited):
          Q.append(node)
          visited.append(node)
      if (item[2]>0 and item[1]<B):
        water=max(min(item[2],B-item[1]),0)
        node=[item[0],item[1]+water,item[2]-water]
        if not (node in visited):
          Q.append(node)
          visited.append(node)
bfs()
results=[]
for item in visited:
  if (item[0]==0 and not item[2] in results):
    results.append(item[2])
results.sort()
for result in results:
  print(result,end=" ")