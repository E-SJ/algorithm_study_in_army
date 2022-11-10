import math
a,b = map(int,input().split())
bin_a=list(map(int,bin(a)[2:]))
bin_b=list(map(int,bin(b+1)[2:]))
pow_2=[2**i for i in range(1000,-1,-1)]
a_pow_2=pow_2[-len(bin_a):]
b_pow_2=pow_2[-len(bin_b):]
temp=0

def cal(start,end,bias):
  temp1=end-start+1
  temp2 = int(math.log((temp1),2))*(temp1)//2
  return temp2+temp1*(bias)


ans1=0
iter=0
for (i,j) in zip(bin_a,a_pow_2):
  if (i*j!=0):
    #print(temp,"~",temp+i*j-1)
    #print(cal(temp,temp+i*j-1,iter))
    ans1+=cal(temp,temp+i*j-1,iter)
    iter+=1
    temp+=i*j
  else:
    pass
    #print("PASS")
#print("ANS",ans1)

ans2=0
iter=0
for (i,j) in zip(bin_b,b_pow_2):
  if (i*j!=0):
    #print(temp,"~",temp+i*j-1)
    #print(cal(temp,temp+i*j-1,iter))
    ans2+=cal(temp,temp+i*j-1,iter)
    iter+=1
    temp+=i*j
  else:
    pass
    #print("PASS")
#print("ANS",ans2)

print(f"{int(ans2-ans1)}")


""" TEST용
0000	0	0000
0001	1	0001				0+1
0010	2	0011				0+1+1
0011	3	0022				0+1+1+2
0100	4	0122				0+1+1+2+1
0101	5	0223				0+1+1+2+1+2
0110	6	0333				0+1+1+2+1+2+2
0111	7	0444	0000			0+1+1+2+1+2+2+3
1000	8	1444	1000			0+1+1+2+1+2+2+3+1
1001	9	2445	2001			0+1+1+2+1+2+2+3+1+2
1010	10	3455	3011			0+1+1+2+1+2+2+3+1+2+2
1011	11	4466	4022	0000		0+1+1+2+1+2+2+3+1+2+2+3
1100	12	5566	5122	1100		0+1+1+2+1+2+2+3+1+2+2+3+2
1101	13	6667	6223	2201	0000	0+1+1+2+1+2+2+3+1+2+2+3+2+3
1110	14	7777	7333	3311	1110	0+1+1+2+1+2+2+3+1+2+2+3+2+3+3
1111	15	8888	8444	4422	2221	0+1+1+2+1+2+2+3+1+2+2+3+2+3+3+4


2~14
0~7
8~11
12~13
14~14
-
0~1

"""