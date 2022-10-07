from bisect import bisect_left, bisect_right
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
p1=0
p2=n-1
result=0
#print(arr)
table=[0 for _ in range(20001)] #실제 값에 10000 더하기
for i in range(-10000,10001,1):
  table[i+10000]=bisect_right(arr,i)-bisect_left(arr,i)
while p1<p2:
  value=-arr[p1]-arr[p2]
  result+=table[value+10000]
  #print(f"we find value:{value} and result:{table[value+10000]} form: ({arr[p1]},{value},{arr[p2]})")
  p2-=1
  p1+=1
print(result)