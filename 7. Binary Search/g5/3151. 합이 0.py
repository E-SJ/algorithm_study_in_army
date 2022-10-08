from bisect import bisect_left, bisect_right
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
result=0
#print(arr)
for i in range(n-2):
  p1=i+1
  p2=n-1
  while p1<p2:
    value=arr[p1]+arr[p2]
    #print(f"we'll compare value {arr[i]}==({-value}) and {arr[p1]},{arr[p2]}")
    if value>-arr[i]:
      p2-=1
    elif value<-arr[i]:
      p1+=1
    else:
      if arr[p1]==arr[p2]:
        result+=p2-p1
        #print(f"same! {arr[i]},{arr[p1]},{arr[p2]} and result:{p2-p1}")
      else:
        temp=p2-bisect_left(arr,arr[p2])+1
        result+=temp
        #print(f"differ! {arr[i]},{arr[p1]},{arr[p2]} and result:{temp}")
      p1+=1
        
  

print(result)