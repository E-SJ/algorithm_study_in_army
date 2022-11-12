import sys
input=sys.stdin.readline
v,e = map(int,input().split())
edges=[]
root_vertex=[i for i in range(v+1)]
for _ in range(e):
  node1,node2,weight = map(int,input().split())
  edges.append((node1,node2,weight))
edges.sort(key=lambda x:x[2])

def find(root_vertex,node):
  if (root_vertex[node]!=node):
    root_vertex[node]=find(root_vertex,root_vertex[node])
  return root_vertex[node]
  
def union(root_vertex,node1,node2):
  root_node1=find(root_vertex,node1)
  root_node2=find(root_vertex,node2)
  if (root_node1>root_node2):
    root_vertex[root_node1]=root_node2
  else:
    root_vertex[root_node2]=root_node1


ans = 0

for node1,node2,weight in edges:
  if (find(root_vertex,node1)!=find(root_vertex,node2)):
    union(root_vertex,node1,node2)
    ans+=weight

print(ans)