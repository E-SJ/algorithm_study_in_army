from bisect import bisect_left, bisect_right
n=int(input())
arr=list(map(int,input().split()))
arr.sort()

ans=0
#print(arr)
for i in range(n-2):
  p1=i+1
  p2=n-1
  while p1<p2:
    if (arr[p1]+arr[p2])>-arr[i]:
      p2-=1
    elif (arr[p1]+arr[p2])<-arr[i]:
      p1+=1
    else:
      #print(arr[i],arr[p1],arr[p2])
      ans+=1
      p1+=1
print(ans)