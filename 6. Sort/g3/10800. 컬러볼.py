import sys
input=sys.stdin.readline
n = int(input())
arr=[]
color_sum=[0 for _ in range(n+1)]
size_count=[0 for _ in range(2001)]
color_size_count=[[0 for _ in range(2001)] for _ in range(n+1)]
for i in range(n):
  c,s = map(int,input().split())
  arr.append([c,s,i,0])
  color_sum[c]+=s
  color_size_count[c][s]+=1
  size_count[s]+=1
sum_color_sum=sum(color_sum)
arr.sort(key=lambda x:(-x[1],x[0]))
#print(*arr)
#print(*color_sum)

for i in range(len(arr)):
  print(size_count[arr[i][1]])
  print(color_size_count[arr[i][0]][arr[i][1]])
  # 아랫부분 처리 필요!!
  arr[i][3]+=sum_color_sum
  arr[i][3]-=color_sum[arr[i][0]]
  arr[i][3]-=arr[i][1]*(size_count[arr[i][1]]-color_size_count[arr[i][0]][arr[i][1]])
  sum_color_sum-=arr[i][1]
  color_sum[arr[i][0]]-=arr[i][1]
  # 윗부분 처리 필요!!
#print(*arr)
arr.sort(key=lambda x:x[2])
for item in arr:
  print(item[3])



""" 시간복잡도 O(N^2) -> 폐기

import sys
input=sys.stdin.readline
n = int(input())
color_arr=[[] for _ in range(n+1)]
arr=[]
for i in range(n):
  c,s = map(int,input().split())
  color_arr[c].append([s,i,0])
  arr.append((c,s))
for i in range(n):
  color_arr[i].sort(reverse=True)
arr.sort(key=lambda x:(x[1],x[0]))

#for color in range(n)
while arr:
  #print(*arr)
  c,s=arr.pop(0)
  for color in range(1,len(color_arr)):
    if (color==c):
      continue
    else:
      for ball in color_arr[color]:
        if (ball[0]>s):
          ball[2]+=s

result_arr=[]
for i in range(len(color_arr)):
  result_arr=result_arr+color_arr[i]
result_arr.sort(key=lambda x:x[1])
for item in result_arr:
  print(item[2])
#print(*arr)

"""