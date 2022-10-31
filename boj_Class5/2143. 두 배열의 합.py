from bisect import bisect_left, bisect_right
from itertools import combinations
t=int(input())
n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))

sum_arr1=[arr1[0]]
for i in range(2,n+1):
  sum_arr1.append(arr1[i-1]+sum_arr1[i-2])
sum_arr2=[arr2[0]]
for i in range(2,m+1):
  sum_arr2.append(arr2[i-1]+sum_arr2[i-2])

case_sum_arr1=[]
case_sum_arr2=[]
for c in combinations(sum_arr1,2):
  case_sum_arr1.append(c[1]-c[0])
for c in combinations(sum_arr2,2):
  case_sum_arr2.append(c[1]-c[0])
for c in combinations(sum_arr1,1):
  case_sum_arr1.append(c[0])
for c in combinations(sum_arr2,1):
  case_sum_arr2.append(c[0])



case_sum_arr1.sort()
case_sum_arr2.sort()
#print(sum_arr1)
#print(case_sum_arr1)
#print(sum_arr2)
#print(case_sum_arr2)

ans = 0
ans_list=[]
for i in range(len(case_sum_arr1)):
  target=t-case_sum_arr1[i]
  case = bisect_right(case_sum_arr2,target) - bisect_left(case_sum_arr2,target)
  ans+=case
  #for j in range(case):
    #ans_list.append([case_sum_arr1[i],case_sum_arr2[bisect_left(case_sum_arr2,target)+j]])

print(ans)
#print(ans_list)


