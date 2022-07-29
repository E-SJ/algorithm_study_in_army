import sys
input=sys.stdin.readline().strip
string = list(input())
stack=[]
for i in range(len(string)):
  if string[i]=='(':
    stack.append(string[i])
  if string[i]=='[':
    stack.append(string[i])
  if string[i]==')':
    if (len(stack)<1 or stack.pop()!='('):
      print('0')
      exit()
  if string[i]==']':
    if (len(stack)<1 or stack.pop()!='['):
      print('0')
      exit()

if (len(stack))!=0:
  print('0')
  exit()


i=0
while True:
  if i == len(string):
    break
  if string[i]=='(':
    stack.append(string[i])
  elif string[i]=='[':
    stack.append(string[i])
  elif string[i]==')':
    item = stack.pop()
    if str(type(item))=="<class 'int'>":
      temp=1
      while str(type(item))=="<class 'int'>":
        temp*=item
        item = stack.pop()
      if len(stack)>=1 and str(type(stack[-1]))=="<class 'int'>":
        stack[-1]+=(temp*2)
      else:
        stack.append(temp*2)
    elif len(stack)>=1 and str(type(stack[-1]))=="<class 'int'>":
      temp=0
      while len(stack)>=1 and str(type(stack[-1]))=="<class 'int'>":
        item = stack.pop()
        temp+=item
      stack.append(temp+2)
    else:
      stack.append(2)
  elif string[i]==']':
    item = stack.pop()
    if str(type(item))=="<class 'int'>":
      temp=1
      while str(type(item))=="<class 'int'>":
        temp*=item
        item = stack.pop()

      if len(stack)>=1 and str(type(stack[-1]))=="<class 'int'>":
        stack[-1]+=(temp*3)
      else:
        stack.append(temp*3)
    elif len(stack)>=1 and str(type(stack[-1]))=="<class 'int'>":
      temp=0
      while len(stack)>=1 and str(type(stack[-1]))=="<class 'int'>":
        item = stack.pop()
        temp+=item
      stack.append(temp+3)
    else:
      stack.append(3)
  i+=1
print(stack[0])


    