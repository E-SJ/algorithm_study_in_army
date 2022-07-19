import sys
input = sys.stdin.readline
t = int(input())
cases=[]
for _ in range(t):
  cases.append(int(input()))


for i in range(t):
  addh=0 #+60
  addt=0 #+10
  mint=0 #-10
  addo=0 #+1
  mino=0 #-1
  if (cases[i]>=36):
    addh+=(cases[i]+24)//60   #1
    cases[i]-=60*addh
    if (cases[i]<-5):
      mint+=((cases[i]-4)//-10)
      cases[i]+=10*mint
    if (cases[i]>5):
      addt+=(cases[i]+4)//10
      cases[i]-=10*addt
    while (cases[i]<0):
      cases[i]+=1
      mino+=1
    while (cases[i]>0):
      cases[i]-=1
      addo+=1
  else:
    if (cases[i]<=5):
      while (cases[i]!=0):
        cases[i]-=1
        addo+=1
    elif (cases[i]>=6):
      while (cases[i]>=6):
        addt+=1
        cases[i]-=10
      while (cases[i]<0):
        cases[i]+=1
        mino+=1
      while (cases[i]>0):
        cases[i]-=1
        addo+=1
  
  print(addh,addt,mint,addo,mino,end="\n")

#문제를 막 풀지 말고 케이스별로 상세하게 나눠서 풀자.
#시간복잡도 낮추기 연습!