import sys


t = int(sys.stdin.readline())
applicants = []
results=[]
for i in range(t):
  results.append(0)
  applicants = []
  n=int(sys.stdin.readline())
  for _ in range(n):
    applicants.append(list(map(int,sys.stdin.readline().split())))
  applicants.sort(key=lambda x:(x[0]))
  cutline=100001
  for j in range(n):
    if (applicants[j][1]<cutline):
      results[i]+=1
      cutline=applicants[j][1]

for result in results:
  print(result)

#pypy3 가 아니라 python3 로 할 수 있을까..?
#https://www.acmicpc.net/status?user_id=7497aaaa&problem_id=1946&from_mine=1
#해결책 -> input() 대신 sys.stdin.readline() 쓰기!!
