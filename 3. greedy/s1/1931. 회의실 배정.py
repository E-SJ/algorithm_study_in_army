n = int(input())
meetings=[]
for i in range(n):
  meetings.append(list(map(int,input().split())))
meetings.sort(key= lambda x: (x[1],x[0]))
empty_time=0
result=0
for [start,end] in meetings:
  if start>=empty_time:
    empty_time=end
    result+=1

print(result)