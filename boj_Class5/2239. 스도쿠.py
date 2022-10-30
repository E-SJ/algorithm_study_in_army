from time import time
import sys
input=sys.stdin.readline
#sys.setrecursionlimit(10**5)
matrix=[]
for _ in range(9):
  matrix.append(list(map(int,input().rstrip())))


cases=[[[1,2,3,4,5,6,7,8,9] for _ in range(9)] for _ in range(9)]

# zone:
# 0 1 2
# 3 4 5
# 6 7 8

def fixmin(arr,num): #NO_USE
  #if num==0, it sames min(arr)
  if (num>=len(arr)):
    raise Exception('BACK TRACKING')
  temp=list(arr)
  for i in range(num):
    temp.remove(min(temp))
  return min(temp)

  
def old_update():
  global empty_loc,matrix,cases
  zones=[{1,2,3,4,5,6,7,8,9} for _ in range(9)]
  for i in range(9):
    for j in range(9):
      cases[i][j]={1,2,3,4,5,6,7,8,9}
      if not (i,j) in empty_loc:
        cases[i][j]=set()
  zones=[{1,2,3,4,5,6,7,8,9} for _ in range(9)]
  for i in range(9):
    for j in range((i//3)*3,(i//3)*3+3):
      for k in range((i%3)*3,(i%3)*3+3):
        zones[i]-={matrix[j][k]}
    for j in range((i//3)*3,(i//3)*3+3):
      for k in range((i%3)*3,(i%3)*3+3):
        cases[j][k]&=zones[i]
  
  for i in range(9):
    for j in range(9):
      for k in range(9):
        cases[i][j]-={matrix[i][k]}
        cases[i][j]-={matrix[k][j]}

def update(start): #복잡도 개선
  global empty_loc,matrix,cases
  i,j = empty_loc[start]

  cases[i][j]=[1,2,3,4,5,6,7,8,9]
  for k in range(9):
    if matrix[i][k] in cases[i][j]:
      cases[i][j].remove(matrix[i][k])
    if matrix[k][j] in cases[i][j]:
      cases[i][j].remove(matrix[k][j])
  if (i//3==0):   #0~2행
    if (j//3==0):   #0~2열
      for row in range(0,3):
        for col in range(0,3):
          if matrix[row][col] in cases[i][j]:
            cases[i][j].remove(matrix[row][col])
    elif (j//3==1):   #3~5열
      for row in range(0,3):
        for col in range(3,6):
          if matrix[row][col] in cases[i][j]:
            cases[i][j].remove(matrix[row][col])
    else:           #6~8열
      for row in range(0,3):
        for col in range(6,9):
          if matrix[row][col] in cases[i][j]:
            cases[i][j].remove(matrix[row][col])
  elif (i//3==1): #3~5행
    if (j//3==0):   #0~2열
      for row in range(3,6):
        for col in range(0,3):
          if matrix[row][col] in cases[i][j]:
            cases[i][j].remove(matrix[row][col])
    elif (j//3==1):   #3~5열
      for row in range(3,6):
        for col in range(3,6):
          if matrix[row][col] in cases[i][j]:
            cases[i][j].remove(matrix[row][col])
    else:           #6~8열
      for row in range(3,6):
        for col in range(6,9):
          if matrix[row][col] in cases[i][j]:
            cases[i][j].remove(matrix[row][col])
  else:           #6~8행
    if (j//3==0):   #0~2열
      for row in range(6,9):
        for col in range(0,3):
          if matrix[row][col] in cases[i][j]:
            cases[i][j].remove(matrix[row][col])
    elif (j//3==1):   #3~5열
      for row in range(6,9):
        for col in range(3,6):
          if matrix[row][col] in cases[i][j]:
            cases[i][j].remove(matrix[row][col])
    else:           #6~8열
      for row in range(6,9):
        for col in range(6,9):
          if matrix[row][col] in cases[i][j]:
            cases[i][j].remove(matrix[row][col])
  
empty_loc=[]
for i in range(9):
  for j in range(9):
    if matrix[i][j]!=0:
      cases[i][j]=[]
    else:
      empty_loc.append((i,j))
update(0)
#print(cases)

def recurse(loc):
  global matrix,cases
  if (loc==len(empty_loc)):
    #print(time()-t)
    for line in matrix:
      print(*line,sep='')
    sys.exit()
  i,j=empty_loc[loc]
  update(loc)

  CASE=cases[i][j]
  for stack in range(len(CASE)):
    #print("DEBUG", loc,"TRYING",stack+1,"/",len(cases[i][j])+stack)
    #update()
    matrix[i][j]=CASE[stack]
    
    #for line in matrix:
      #print(*line,sep='')
    #print("")
    #if (loc+1<len(empty_loc)):
    #  update(loc+1)

    recurse(loc+1)
    matrix[i][j]=0
    #CASE.remove(CASE[0])
    """
    if (recurse(loc+1)==-1):
      #print(CASE)
      matrix[i][j]=0
      #update()
      CASE-={min(CASE)}
      continue
    else:
      break
    """
    

t=time()
recurse(0)

#print(matrix)