n = int(input())
A,B,C,D,E,F= map(int,input().split())

see3 = min(E+F+C,C+B+F,B+D+F,E+D+F,E+A+C,A+B+C,B+D+A,D+E+A)
see2 = min(E+F,C+F,B+F,F+D,E+A,C+A,A+B,D+A,E+D,E+C,C+B,B+D)
see1 = min(A,B,C,D,E,F)
see5 = A+B+C+D+E+F - max(A,B,C,D,E,F)

if n==1:
  result=see5
else:
  result=see3*4
  result+=see2*((n-2)*(4)+(n-1)*(4))
  result+=see1*((n-2)*(n-1)*(4)+((n-2)**2))

print(result)

#아이디어: 주사위 및 정육면체 구조를 잘 생각하여 공식을 일반화만 잘 시키면 된다!