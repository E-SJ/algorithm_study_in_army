n = int(input())
h,m,s,count=0,0,0,0
for _ in range(n*3600+3600):
  s+=1
  if s==60:
    m+=1
    s=0
    if m==60:
      h+=1
      m=0
  if (h%10==3) or (m//10==3) or (m%10==3) or (s//10==3) or (s%10==3):
    count+=1
    
print(count)