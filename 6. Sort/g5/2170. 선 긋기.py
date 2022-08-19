import sys
input=sys.stdin.readline
n = int(input())
lines=[]

for _ in range(n):
  lines.append(list(map(int,input().split())))
      
lines.sort(key=lambda x:(x[0],x[1]))
#print(lines)
result=0
min=lines[0][0]
max=lines[0][1]
#print("ADD",max-min)
result+=max-min
for i in range(1,n):
  if (min<=lines[i][0]<=max and max<lines[i][1]):
    #print("ADD1",lines[i][1]-max,min,max)
    result+=lines[i][1]-max
    min=lines[i][0]
    max=lines[i][1]
  elif (min<=lines[i][0]<=max and max>=lines[i][1]):
    pass
  else:
    min=lines[i][0]
    max=lines[i][1]
    #print("ADD2",max-min,min,max)
    result+=max-min
print(result)