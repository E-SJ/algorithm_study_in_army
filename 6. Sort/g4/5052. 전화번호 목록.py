import sys
input=sys.stdin.readline
t = int(input())
for _ in range(t):
  breakflag=False
  arr=[]
  n = int(input())
  for _ in range(n):
    arr.append(input().rstrip())
  arr.sort()
  for i in range(n-1):
    #print(arr[i] , arr[i+1][:len(arr[i])])
    if arr[i] == arr[i+1][:len(arr[i])]:
      print("NO")
      break
  else:
    print("YES")