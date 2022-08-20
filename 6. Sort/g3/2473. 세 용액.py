import sys
input = sys.stdin.readline
n = int(input())
att=list(map(int,input().split()))
att.sort()
ans=3000000000

#print_arr(att)
#print()
for pivot in range(n-2):
  point1=pivot+1
  point2=n-1
  fix = att[pivot]
  while point1 < point2:
    #print_arr(sorted([att[point1],att[point2],att[pivot]]))
    #print()
    p1,p2=att[point1],att[point2]
    temp = p1+p2+fix
    if (abs(temp)<abs(ans)):
        ans=abs(temp)
        left,mid,right=fix,p1,p2
    if (temp>0):
      point2-=1
    elif (temp<0):
      point1+=1
    else:
      print(fix,p1,p2)
      exit()

#print(ans)
print(left,mid,right)