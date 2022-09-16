n,m,k = map(int,input().split())

if k!=0:
  target_y,target_x=(k-1)//m+1,(k-1)%m+1
  matrix=[[0 for _ in range(target_x+1)] for _ in range(target_y+1)]
  matrix[0][1]=1
  
  for step in range(min(target_y,target_x)):
    for c in range(step+1,target_x+1):
      matrix[step+1][c] = matrix[step][c]+matrix[step+1][c-1]
    for r in range(step+1,target_y+1):
      matrix[r][step+1] = matrix[r][step]+matrix[r-1][step+1]
  result_1 = matrix[target_y][target_x]
  
  
  target_y,target_x = n-target_y+1, m-target_x+1
  matrix=[[0 for _ in range(target_x+1)] for _ in range(target_y+1)]
  matrix[0][1]=1
  
  for step in range(min(target_y,target_x)):
    for c in range(step+1,target_x+1):
      matrix[step+1][c] = matrix[step][c]+matrix[step+1][c-1]
    for r in range(step+1,target_y+1):
      matrix[r][step+1] = matrix[r][step]+matrix[r-1][step+1]
  result_2 = matrix[target_y][target_x]
  print(result_1*result_2)
else:
  target_y,target_x=m,n
  matrix=[[0 for _ in range(target_x+1)] for _ in range(target_y+1)]
  matrix[0][1]=1
  
  for step in range(min(target_y,target_x)):
    for c in range(step+1,target_x+1):
      matrix[step+1][c] = matrix[step][c]+matrix[step+1][c-1]
    for r in range(step+1,target_y+1):
      matrix[r][step+1] = matrix[r][step]+matrix[r-1][step+1]
  print(matrix[target_y][target_x])
  
  
    

    
    
  