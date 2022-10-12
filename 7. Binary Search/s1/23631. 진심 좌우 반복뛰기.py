import sys
input=sys.stdin.readline
t=int(input())
weight=[0]
pos=[0]
direction=['R','L'] # 짝수 인덱스면 오른쪽(+1), 홀수 인덱스면 왼쪽(-1)
for i in range(0,4999):
  weight.append((1+i//2)*(-1)**(i%2))
  pos.append(pos[-1]+i+1)
  
for _ in range(t):
  n,k=map(int,input().split())
  left=0
  right=4999
  ans=0
  while left<=right:
    mid=(left+right)//2
    if (pos[mid]*k>n-1):
      right=mid-1
    elif (pos[mid]*k<n-1):
      ans=max(ans,mid)
      left=mid+1
    else:
      print(weight[mid]*k,direction[mid%2])
      break
  else:
    print(weight[ans]*k+(-1)**(ans%2)*(n-1-pos[ans]*k),direction[(ans)%2])


  