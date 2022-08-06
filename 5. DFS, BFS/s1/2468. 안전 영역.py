import sys
sys.setrecursionlimit(10**6)
def water(h):
  for y in range(n):
    for x in range(n):
      if (matrix[y][x]>=h):
        check[y][x]=1

def reset():
  check = [[0 for _ in range(n)] for _ in range(n)]

def dfs(y,x,num):
  check[y][x]=num
  for k in range(4):
    if (0<=y+dy[k]<n and 0<=x+dx[k]<n and check[y+dy[k]][x+dx[k]]==1):
      dfs(y+dy[k],x+dx[k],num)
      

n = int(input())
matrix = []
heights=[]
for _ in range(n):
  matrix.append(list(map(int,input().split())))

check = [[0 for _ in range(n)] for _ in range(n)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

for h in range(100):
  water(h)
  areanum=2 # 0은 물에 잠김, 1은 물에 안잠김, 2부터 안잠긴 영역의 번호
  for y in range(n):
    for x in range(n):
      if (check[y][x]==1):
        dfs(y,x,areanum)
        areanum+=1
  
  heights.append(areanum-2)
  reset()
  if (areanum-2==0):
    break

print(max(heights))