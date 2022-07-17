n = int(input())
elems = list(map(int,input().split()))
s = int(input())
count=0
for i in range(n):
  if (elems.index(sorted(elems)[-i-1])-i<=s):
    for j in range(elems.index(sorted(elems)[-i-1])-1,-1+i,-1):
      temp=elems[j]
      elems[j]=elems[j+1]
      elems[j+1]=temp
      count+=1
      s-=1
      print("DEBUG1")
      if (s<=0):
        break
  else:
    print(sorted(elems)[count+s]-1+count,count,-1)
    for j in range(elems.index(sorted(elems)[count+s])-1+count,count,-1):
      temp=elems[j]
      elems[j]=elems[j+1]
      elems[j+1]=temp
      s-=1
      print("DEBUG2")
      if (s<=0):
        break
  if (s<=0):
    break

for elem in elems:
  if (elem==elems[-1]):
    print(elem,end='')
  else:
    print(elem,end=' ')