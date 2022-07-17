n,k = map(int,input().split())
heights = list(map(int,input().split()))
differences=[]
for i in range(n-1):
  differences.append(heights[i+1]-heights[i])
differences.sort()
result=0
for i in range(n-k):
  result+=differences[i]

print(result)

#아이디어: 2212번 문제와 아이디어가 똑같다! 4분만에 푼듯..