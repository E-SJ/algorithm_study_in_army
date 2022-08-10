from sys import setrecursionlimit
setrecursionlimit(10**6)
n,m =map(int,input().split())
friends=[[] for _ in range(n)]
for _ in range(m):
  a,b=map(int,input().split())
  friends[a].append(b)
  friends[b].append(a)


def dfs(a=-1,b=-1,c=-1,d=-1,e=-1):
  if (b==-1):
    if friends[a]!=[]:
      for item in friends[a]:
        dfs(a,item)
  
  elif (c==-1):
    if friends[b]!=[]:
      for item in friends[b]:
        if (item!=a):
          dfs(a,b,item)
  
  elif (d==-1):
    if friends[c]!=[]:
      for item in friends[c]:
        if (item!=a and item!=b):
          dfs(a,b,c,item)
          
  elif (e==-1):
    if friends[d]!=[]:
      for item in friends[d]:
        if (item!=a and item!=b and item!=c):
          dfs(a,b,c,d,item)
  else:
    print(1)
    exit()
  
    
for i in range(n):
  dfs(i)

print(0)

