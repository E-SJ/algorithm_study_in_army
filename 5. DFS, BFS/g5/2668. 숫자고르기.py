from sys import setrecursionlimit
setrecursionlimit(10**6)
n = int(input())
table = [[] for _ in range(n+1)]
for i in range(n):
  table[i+1]=int(input())

result = []
def dfs(n,visit):
  visit.append(n)
  #print(visit)
  if (n==table[n]):
    result.append(n)
    #print("ADD", visit[visit.index(table[n]):])
    return
  if not table[n] in visit:
    dfs(table[n],visit.copy())
  if table[n] in visit:
    result.extend(visit[visit.index(table[n]):])
    #print("ADD", visit[visit.index(table[n]):])

for i in range(1,n+1):
  dfs(i,[])

result=list(set(result))
result.sort()
print(len(result))
for item in result:
  print(item)