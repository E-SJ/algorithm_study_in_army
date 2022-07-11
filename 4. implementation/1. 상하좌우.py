n = int(input())
tomove = list(map(str, input().split()))
x,y=1,1
for i in range(len(tomove)):
  if tomove[i]=='U' and y>1:
    y-=1
  elif tomove[i]=='D' and y<n:
    y+=1
  elif tomove[i]=='L' and x>1:
    x-=1
  elif tomove[i]=='R' and x<n:
    x+=1

print(y,x)
    