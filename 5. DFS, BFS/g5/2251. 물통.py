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
      print(item)
      AB = abs(item[0]-item[1])
      BC = abs(item[1]-item[2])
      AC = abs(item[2]-item[0])
      if (item[0]==A):
        if not ([item[0]-AB,item[1]+AB,item[2]] in visited):
          Q.append([item[0]-AB,item[1]+AB,item[2]])
          visited.append([item[0]-AB,item[1]+AB,item[2]])
        if not ([item[0]-AC,item[1],item[2]+AC] in visited):
          Q.append([item[0]-AC,item[1],item[2]+AC])
          visited.append([item[0]-AC,item[1],item[2]+AC])
      elif (item[1]==B):
        if not ([item[0]+AB,item[1]-AB,item[2]] in visited):
          Q.append([item[0]+AB,item[1]-AB,item[2]])
          visited.append([item[0]+AB,item[1]-AB,item[2]])
        if not ([item[0],item[1]-BC,item[2]+BC] in visited):
          Q.append([item[0],item[1]-BC,item[2]+BC])
          visited.append([item[0],item[1]-BC,item[2]+BC])
        
      elif (item[2]==C):
        if not ([item[0]+AC,item[1],item[2]-AC] in visited):
          Q.append([item[0]+AC,item[1],item[2]-AC])
          visited.append([item[0]+AC,item[1],item[2]-AC])
        if not ([item[0],item[1]+BC,item[2]-BC] in visited):
          Q.append([item[0],item[1]+BC,item[2]-BC])
          visited.append([item[0],item[1]+BC,item[2]-BC])
bfs()
print(visited)