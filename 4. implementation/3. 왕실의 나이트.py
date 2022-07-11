string=list(input())
col = int(ord(string[0]))-int(ord('a'))+1
row = int(string[1])
move=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
count=0
for d_col,d_row in move:
  if (col+d_col)>=1 and (col+d_col)<=8 and (row+d_row)>=1 and (row+d_row)<=8:
    count+=1

print(count)