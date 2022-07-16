n = int(input())
k = int(input())
sensors = list(map(int,input().split()))
sensors.sort()
distances = []
for i in range(n-1):
  distances.append(sensors[i+1]-sensors[i])
distances.sort()
result=0
for i in range(n-k):
  result+=distances[i]

print(result)


# 아이디어 : 집중국의 위치에 신경쓰지 않고, 센서 시작 부분에서 센서 끝 지점까지, 집중국의 신호가 안닿아도 되는 부분을 "최대화" 시킨다고 생각하자. (이는 집중국의 신호가 닿아야 하는 부분을 "최소화"와 같다.)
# 따라서, 센서가 10개, 집중국이 5개이면, 각 센서간의 구간은 총 9개이고, 집중국이 닿아야하는 구간의 개수는 집중국의 개수인 5개이므로 집중국이 안닿아도 되는 구간의 개수는 4개이다.
# 이때 우리는 집중국이 안닿아도 되는 구간을 최대화 시킨다고 했으므로, 각 구간의 길이가 가장 큰 것을 집중국이 안닿아도 되는 구간으로 잡는다.
# 그렇게 되면 각 센서들의 구간 9개에서 가장 큰 길이의 구간 4개를 배제하여 5개의 구간의 각 길이의 합이 곧 답이된다.


  