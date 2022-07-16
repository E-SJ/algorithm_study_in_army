s = input()
t = input()

def rev_1(t):
  return t[0:-1]
def rev_2(t):
  text = t[0:-1]
  return text[::-1]

result=0
for _ in range(len(t)-len(s)):
  if (t[-1]=='A'):
    t=rev_1(t)
  elif (t[-1]=='B'):
    t=rev_2(t)
  if (s==t):
    result=1

print(result)

#아이디어 : s -> t를 생각하지 말고, t->s를 생각하자!