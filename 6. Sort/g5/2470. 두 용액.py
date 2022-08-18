n = int(input())
att=list(map(int,input().split()))
att.sort()
point1=0
point2=n-1
sum = att[point1]+att[point2]
result_value=sum
result_index=[point1,point2]
while point1!=point2:
  sum = att[point1]+att[point2]
  if (abs(result_value)>abs(sum)):
    result_value=sum
    result_index[0],result_index[1] = point1,point2
  if (sum<0):
    point1+=1
  elif (sum>0):
    point2-=1
  else:
    print(att[result_index[0]],att[result_index[1]])
    exit()
print(att[result_index[0]],att[result_index[1]])