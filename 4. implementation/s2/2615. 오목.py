omok=[]
for _ in range(19):
  omok.append(list(map(int,input().split())))

for i in range(19):
  for j in range(19):
    if (omok[i][j]==1):
      if (i<15 and j<15):
        if ((omok[i+1][j+1]==1) and (omok[i+2][j+2]==1) and(omok[i+3][j+3]==1) and(omok[i+4][j+4]==1)):
          
          if (i+5<19 and j+5<19):
            if (omok[i+5][j+5]==1):
              continue
          if (i-1>=0 and j-1>=0):
            if (omok[i-1][j-1]==1):
              continue

          print(omok[i][j])
          print(i+1,j+1)
          exit()
      if (i>3 and j<15):
        if ((omok[i-1][j+1]==1) and (omok[i-2][j+2]==1) and(omok[i-3][j+3]==1) and(omok[i-4][j+4]==1)):
          if (i-5>=0 and j+5<19):
            if (omok[i-5][j+5]==1):
              continue
          if (i+1<19 and j-1>=0):
            if (omok[i+1][j-1]==1):
              continue
          print(omok[i][j])
          print(i+1,j+1)
          exit()
      if (i<15):
        if ((omok[i+1][j]==1) and (omok[i+2][j]==1) and(omok[i+3][j]==1) and(omok[i+4][j]==1)):
          if (i+5<19):
            if (omok[i+5][j]==1):
              continue
          if (i-1>=0):
            if (omok[i-1][j]==1):
              continue
          print(omok[i][j])
          print(i+1,j+1)
          exit()
      if (j<15):
        if ((omok[i][j+1]==1) and (omok[i][j+2]==1) and(omok[i][j+3]==1) and(omok[i][j+4]==1)):
          if (j+5<19):
            if (omok[i][j+5]==1):
              continue
          if (j-1>=0):
            if (omok[i][j-1]==1):
              continue
          print(omok[i][j])
          print(i+1,j+1)
          exit()
      
    if (omok[i][j]==2):
      if (i<15 and j<15):
        if ((omok[i+1][j+1]==2) and (omok[i+2][j+2]==2) and(omok[i+3][j+3]==2) and(omok[i+4][j+4]==2)):
          if (i+5<19 and j+5<19):
            if (omok[i+5][j+5]==2):
              continue
          if (i-1>=0 and j-1>=0):
            if (omok[i-1][j-1]==2):
              continue
          print(omok[i][j])
          print(i+1,j+1)
          exit()
      if (i>3 and j<15):
        if ((omok[i-1][j+1]==2) and (omok[i-2][j+2]==2) and(omok[i-3][j+3]==2) and(omok[i-4][j+4]==2)):
          if (i-5>=0 and j+5<19):
            if (omok[i-5][j+5]==2):
              continue
          if (i+1<19 and j-1>=0):
            if (omok[i+1][j-1]==2):
              continue
          print(omok[i][j])
          print(i+1,j+1)
          exit()
      if (i<15):
        if ((omok[i+1][j]==2) and (omok[i+2][j]==2) and(omok[i+3][j]==2) and(omok[i+4][j]==2)):
          if (i+5<19):
            if (omok[i+5][j]==2):
              continue
          if (i-1>=0):
            if (omok[i-1][j]==2):
              continue
          print(omok[i][j])
          print(i+1,j+1)
          exit()
      if (j<15):
        if ((omok[i][j+1]==2) and (omok[i][j+2]==2) and(omok[i][j+3]==2) and(omok[i][j+4]==2)):
          if (j+5<19):
            if (omok[i][j+5]==2):
              continue
          if (j-1>=0):
            if (omok[i][j-1]==2):
              continue
          print(omok[i][j])
          print(i+1,j+1)
          exit()
          
print(0)