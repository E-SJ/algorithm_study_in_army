n = int(input())

if (n%5)==0:
  a = n//5
  b = 0
elif (n%5)==1:
  a = n//5 - 1
  if (a<0):
    print("-1")
    exit()
  else:
    b = 2 #(=6/2)
elif (n%5)==2:
  a = n//5 - 2
  if (a<0):
    print("-1")
    exit()
  else:
    b = 4 #(=12/3)
elif (n%5)==3:
  a = n//5
  b = 1 #(=3/3)
elif (n%5)==4:
  a = n//5 - 1
  if (a<0):
    print("-1")
    exit()
  else:
    b = 3 #(=9/3)

print(a+b)
  