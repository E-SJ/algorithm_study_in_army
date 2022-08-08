from collections import deque

tree=[[] for i in range(150)]
def appendtree(parent):
  if parent==-1:
    tree[1]=[-1,-1]
  else:
    if tree[parent*2]==[]:
      tree[parent].
      tree[parent*2]=[-1,-1]
    else:
        


def deletenode(initnode):
  initnode+=1
  Q.append(initnode)
  while len(Q):
    for i in range(len(Q)):
      node=Q.popleft()
      tree[node]=0
      if (node*2<=50):
        Q.append(node*2)
      if (node*2+1<=50):
        Q.append(node*2+1)


def cal_leaf():
  result=0
  for i in range(1,51):
    if (tree[i]==1 and (tree[i*2]==0 and tree[i*2+1]==0)):
        result+=1
  return result
        
Q=deque()
n = int(input())
nodes=list(map(int,input().split()))
for node in nodes:
  appendtree(node)

deletenode(int(input()))
leafnodes=cal_leaf()
print(leafnodes)
print(level())
print(tree)