n=int(input())
matrix=[]
for _ in range(n):
  name,score = map(str,input().split())
  matrix.append([name,int(score)])

matrix.sort(key=lambda x:(x[1]))
for i in range(n):
  print(matrix[i][0],end=" ")