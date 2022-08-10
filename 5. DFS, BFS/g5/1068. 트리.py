from collections import deque

def delnode(node):
  Q.append(node)
  while (len(Q)):
    for _ in range(len(Q)):
      nodenum=Q.popleft()
      tree[nodenum]=-2
      for i in range(len(tree)):
        if (tree[i]==nodenum):
          Q.append(i)


Q=deque()
n = int(input())
tree=list(map(int,input().split()))
delnode(int(input()))
count=0
for i in range(len(tree)):
  if (tree[i]!=-2):
    if i in tree: 
      pass
    else:
      count+=1

print(count)


