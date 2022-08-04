import copy
import sys
sys.setrecursionlimit(50000000)
n=int(input())
colors=[]
for _ in range(n):
  colors.append(list(map(str,input())))
colors_2=copy.deepcopy(colors)
for y in range(n):
  for x in range(n):
    if (colors_2[y][x] == 'G'):
      colors_2[y][x] = 'R'
    

def RGB(y,x,count,color):
  if (colors[y][x]==color):
    colors[y][x]=count
    if(y>0 and (colors[y-1][x]=='R' or colors[y-1][x]=='G' or colors[y-1][x]=='B')):
      RGB(y-1,x,count,color)
    if(y<n-1 and (colors[y+1][x]=='R' or colors[y+1][x]=='G' or colors[y+1][x]=='B')):
      RGB(y+1,x,count,color)
    if(x>0 and (colors[y][x-1]=='R' or colors[y][x-1]=='G' or colors[y][x-1]=='B')):
      RGB(y,x-1,count,color)
    if(x<n-1 and (colors[y][x+1]=='R' or colors[y][x+1]=='G' or colors[y][x+1]=='B')):
      RGB(y,x+1,count,color)

def RB(y,x,count,color):
  if (colors_2[y][x]==color):
    colors_2[y][x]=count
    if(y>0 and (colors_2[y-1][x]=='R' or colors_2[y-1][x]=='G' or colors_2[y-1][x]=='B')):
      RB(y-1,x,count,color)
    if(y<n-1 and (colors_2[y+1][x]=='R' or colors_2[y+1][x]=='G' or colors_2[y+1][x]=='B')):
      RB(y+1,x,count,color)
    if(x>0 and (colors_2[y][x-1]=='R' or colors_2[y][x-1]=='G' or colors_2[y][x-1]=='B')):
      RB(y,x-1,count,color)
    if(x<n-1 and (colors_2[y][x+1]=='R' or colors_2[y][x+1]=='G' or colors_2[y][x+1]=='B')):
      RB(y,x+1,count,color)
      

count1=0
for y in range(n):
  for x in range(n):
    if (colors[y][x]=='R' or colors[y][x]=='G' or colors[y][x]=='B'):
      RGB(y,x,count1,colors[y][x])
      count1+=1

print(count1,end=" ")

count2=0
for y in range(n):
  for x in range(n):
    if (colors_2[y][x]=='R' or colors_2[y][x]=='G' or colors_2[y][x]=='B'):
      RB(y,x,count2,colors_2[y][x])
      count2+=1
print(count2)