n = int(input())
total_recommend= int(input())
recommends=list(map(int,input().split()))
photoes=[] #학생번호, 추천수, 게시된 시각
for i in range(total_recommend):
  if (len(photoes)==0):#비었을때
    photoes.append([recommends[i],1,i])
  else:
    for j in range(len(photoes)):
      if photoes[j][0]==recommends[i]: #찾았을때
        photoes[j][1]+=1
        break
      if (j==len(photoes)-1): #못찾았을 때
        if (len(photoes)<n): #빈공간이 있다면
          photoes.append([recommends[i],1,i])
        else: #빈공간이 없다면
          photoes.sort(key=lambda x:(-x[1],-x[2]))
          photoes[n-1]=[recommends[i],1,i]

photoes.sort(key=lambda x:(x[0]))
for item in photoes:
  print(item[0],end=" ")