n = int(input())
point=[]
for _ in range(n):
  point.append(tuple(map(int,input().split())))
point.sort(key=lambda x:(x[0],x[1]))
print(point)
