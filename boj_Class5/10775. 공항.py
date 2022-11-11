import sys
sys.setrecursionlimit(10**5+100)
input=sys.stdin.readline
g=int(input())
p=int(input())
planes=[]
for _ in range(p):
  planes.append(int(input()))
                    
gates=[i for i in range(100001)]

def find_parent(nodenum):
  global gates
  if (gates[nodenum]!=nodenum):
    gates[nodenum] = find_parent(gates[nodenum])
  return gates[nodenum]

def union_parent(nodenum1,nodenum2):
  global gates
  gates[find_parent(nodenum1)]=find_parent(nodenum2)
  
count=0
#print(gates[:g+1])

for plane in planes:
  p_plane=find_parent(plane)
  if p_plane==0:
    break
  union_parent(p_plane,p_plane-1)
  count+=1
  #print(gates[:g+1])
print(count)