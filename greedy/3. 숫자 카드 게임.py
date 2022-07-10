n,m = map(int,input().split())

cards = []
for i in range(n):
  cards.append(list(map(int,input().split())))

mins=[]
for i in range(n):
  mins.append(min(cards[i]))

print (max(mins))

