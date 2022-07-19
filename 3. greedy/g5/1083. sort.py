n = int(input())
elems = list(map(int,input().split()))
s = int(input())
count=0
for i in range(n):
  if (s==0):
    break
  #print(f"s={s} len(elems) = {len(elems)}")
  #print(elems[i:i+min(s+1,len(elems))])
  #print(elems)
  
  maxvalue = max(elems[i:i+min(s+1,len(elems))])
  if (elems[i]>=maxvalue):
    continue
  else:
    #print(maxvalue)
    for j in range(elems.index(maxvalue),i,-1):
      if (s==0):
        break
      temp = elems[j]
      elems[j] = elems[j-1]
      elems[j-1]=temp
      s-=1
  if (s==0):
    break

for i in range(n):
  if (i==n-1):
    print(elems[i],end="")
  else:
    print(elems[i],end=" ")

#아이디어 : 문제를 너무 복잡하게 생각한 것이 화근이었다.
#옮길수 있는 s의 값에 따라서 이동시킬 수 있는 최대값을 정하여 맨 앞으로 옮긴다. n<=s-1 라면 당연히 뭐든 맨 앞으로 이동시킬 수 있을 것이고, n>s-1 이라면 s에 값에 따라 인덱스 범위를 조절하고, 만약 s가 남는다면 똑같이 시행하면 s는 곧 0이 될 것이다.