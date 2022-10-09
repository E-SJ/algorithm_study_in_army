#""" MITM + 투포인터
from itertools import combinations
n,s = map(int,input().split())
arr=list(map(int,input().split()))
arr_l=arr[:n//2]
arr_r=arr[n//2:]
freq_l=[]
freq_r=[]
    
for i in range(0,len(arr_l)+1):
  for comb in combinations(arr_l,i):
    freq_l.append(sum(comb))


for i in range(0,len(arr_r)+1):
  for comb in combinations(arr_r,i):
    freq_r.append(sum(comb))
#print(freq_l)
#print(freq_r)
freq_l.sort()
freq_r.sort()
ans=0

p1=0 # 0->len(freq_l)
p2=len(freq_r)-1 # len(freq_r)-1->-1
while p1<len(freq_l) and p2>=0:
  value=freq_l[p1]+freq_r[p2]
  if (value==s):
    count_l=1
    count_r=1
    while p1+count_l<len(freq_l) and freq_l[p1+count_l]==freq_l[p1]:
      count_l+=1
    while p2-count_r>=0 and freq_r[p2-count_r]==freq_r[p2]:
      count_r+=1
    ans+=count_l*count_r
    p1+=count_l
    p2-=count_r
  elif (value<s):
    p1+=1
  elif (value>s):
    p2-=1
if (s==0):
  ans-=1
print(ans)

""" MITM + 이분 탐색
from itertools import combinations
from bisect import bisect_left,bisect_right
n,s = map(int,input().split())
arr=list(map(int,input().split()))
arr_l=arr[:n//2]
arr_r=arr[n//2:]
freq_l=[]
freq_r=[]
def cal_count(arr,value):
  return bisect_right(arr,value) - bisect_left(arr,value)
    
for i in range(0,len(arr_l)+1):
  for comb in combinations(arr_l,i):
    freq_l.append(sum(comb))


for i in range(0,len(arr_r)+1):
  for comb in combinations(arr_r,i):
    freq_r.append(sum(comb))
#print(freq_l)
#print(freq_r)
freq_l.sort()
freq_r.sort()
ans=0
for freq in freq_l:
  ans+=cal_count(freq_r,s-freq)
    
if (s==0):
  ans-=1
print(ans)
"""

""" 좀 더 직관적인 MITM + HASH(dict)
from bisect import bisect_left
n,s = map(int,input().split())
arr=list(map(int,input().split()))
arr_l=arr[:n//2]
arr_r=arr[n//2:]
freq_l={}
freq_r={}
    
for i in range(0,len(arr_l)+1):
  for comb in combinations(arr_l,i):
    try:
      freq_l[sum(comb)]+=1
    except:
      freq_l[sum(comb)]=1

for i in range(0,len(arr_r)+1):
  for comb in combinations(arr_r,i):
    try:
      freq_r[sum(comb)]+=1
    except:
      freq_r[sum(comb)]=1
#print(freq_l)
#print(freq_r)
ans=0
for key in freq_l.keys():
  try:
    ans+=freq_l[key]*freq_r[s-key]
  except:
    pass
    
if (s==0):
  ans-=1
print(ans)
"""

""" MITM(중간에서 만나기) + HASH(dict)
from itertools import combinations
n,s = map(int,input().split())
arr=list(map(int,input().split()))
arr_l=arr[:n//2]
arr_r=arr[n//2:]
freq={}


for i in range(0,len(arr_l)+1):
  for comb in combinations(arr_l,i):
    try:
      freq[sum(comb)]+=1
    except:
      freq[sum(comb)]=1
    
    
ans=0

for i in range(0,len(arr_r)+1):
  for comb in combinations(arr_r,i):
    try:
      ans+=freq[s-sum(comb)]
    except:
      pass
if (s==0):
  ans-=1
print(ans)
"""