string = list(input())
small_count=0
big_count=0
recent=""
for i in range(len(string)):
  if string[i]=='(':
    small_count+=1
    recent='small'
  if string[i]=='[':
    big_count+=1
    recent='big'
  if string[i]==')':
    if small_count<1:
      print('0')
      exit()
    else:
      small_count-=1
  if string[i]==']':
    if big_count<1:
      print('0')
      exit()
    else:
      big_count-=1
  print(big_count,small_count)
if (small_count!=0) or (big_count!=0):
  print("debug")
  print('0')
  exit()

cal=[]
while True:
  count=0
  find_flag=False
  for i in range(len(string)-1):
    if string[i]+string[i+1]=='()':
      string[i] = count
      count+=1
      del string[i+1]
      cal.append(2)
      find_flag=True
    if string[i]+string[i+1]=='[]':
      string[i] = count
      count+=1
      del string[i+1]
      cal.append(3)
      find_flag=True
    print(string)
  if (find_flag==False):
    break
    


    