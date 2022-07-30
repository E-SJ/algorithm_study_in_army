n,w,l = map(int,input().split())
weights=list(map(int,input().split()))
#n = 다리를 건너는 트럭의 수
#w = 다리의 길이
#l = 다리의 최대 하중
#weights = 각 트럭의 무게

on_bridge=[]
complete=[-1]
time = 0
while len(complete)<=n:
  for i in range(complete[-1]+1,len(weights)): # 각 트럭에 대해
    if (len(on_bridge)>0 and i in list(zip(*on_bridge))[0]): #다리위에 있으면
      if (on_bridge[list(zip(*on_bridge))[0].index(i)][1]<w): #아직 거리가 남았다면
        on_bridge[list(zip(*on_bridge))[0].index(i)][1]+=1
      else: #다리를 다 건넜다면
        del on_bridge[list(zip(*on_bridge))[0].index(i)]
        complete.append(i)
    elif (len(on_bridge)==0) or (len(on_bridge)>0 and sum(list(zip(*on_bridge))[2])+weights[i]<=l): #다리에 아무도 없거나, 자신이 다리위에 없는데 다리에 올라갈 수 있다면
      on_bridge.append([i,1,weights[i]]) # 차량번호, 다리에서의 위치, 차량의 무게
      break #다리에 올라 탔다면 동시에 여러 차가 못타므로 루프 종료.
    else: #다리위에 없으나 다리에 올라갈 수도 없다면
      break #그 뒤는 당연히 못올라가므로 루프 종료.
  time+=1

print(time)

    
