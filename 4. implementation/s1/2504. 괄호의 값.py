string = list(input())
small_count=0
big_count=0
for i in range(len(string)):
  if string[i]=='(':
    small_count+=1
  if string[i]=='[':
    big_count+=1
  if string[i]==')':
    small_count-=1
  if string[i]==']':
    big_count-=1
if (small_count!=0) or (big_count!=0):
  print('0')
  exit()

while True:
  i=0
  while True:
    if (i>=len(string)-1):
      break
    if str(string[i])+str(string[i+1])=='()':
      string[i] = 2
      del string[i+1]
    if (i>=len(string)-1):
      break
    if str(string[i])+str(string[i+1])=='[]':
      string[i] = 3
      del string[i+1]
    if (i>=len(string)-1):
      break
    if ((str(type(string[i]))=="<class 'int'>") and (str(type(string[i+1]))=="<class 'int'>")):
      string[i]+=string[i+1]
      del string[i+1]
    i+=1
  i=0
  while True:
    if (i>=len(string)-2):
      break
    if str(string[i])+str(string[i+2])=='()':
      string[i]=string[i+1]*2
      del string[i+2]
      del string[i+1]
    if (i>=len(string)-2):
      break
    if str(string[i])+str(string[i+2])=='[]':
      string[i]=string[i+1]*3
      del string[i+2]
      del string[i+1]
    i+=1
  i=0
    
  if (len(string)==1):
    break

print(string[0])


    