import sys
sys.setrecursionlimit(10**5)
matrix=[]
for _ in range(9):
  matrix.append(list(map(int,input())))


cases=[[{1,2,3,4,5,6,7,8,9} for _ in range(9)] for _ in range(9)]

# zone:
# 0 1 2
# 3 4 5
# 6 7 8

def fixmin(arr,num):
  #if num==0, it sames min(arr)
  if (num>=len(arr)):
    raise Exception('BACK TRACKING')
  temp=list(arr)
  for i in range(num):
    temp.remove(min(temp))
  return min(temp)

  
def update():
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



empty_loc=[]
for i in range(9):
  for j in range(9):
    if matrix[i][j]!=0:
      cases[i][j]=set()
    else:
      empty_loc.append((i,j))
update()
#print(cases)

def recurse(loc):
  global matrix,cases
  if (loc==len(empty_loc)):
    for line in matrix:
      print(*line,sep='')
    exit()
  i,j=empty_loc[loc]
  update()
  if len(cases[i][j])==0:
    return -1
  CASE=cases[i][j]
  for stack in range(len(CASE)):
    update()
    matrix[i][j]=min(CASE)
    #for line in matrix:
      #print(*line,sep='')
    #print("")
    if (recurse(loc+1)==-1):
      #print(CASE)
      matrix[i][j]=0
      update()
      CASE-={min(CASE)}
      continue
    else:
      break
    
  else:
    return -1


recurse(0)

#print(matrix)