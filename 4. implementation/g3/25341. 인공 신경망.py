import sys
input=sys.stdin.readline
n,m,q = map(int,input().split()) # 입력 크기, 은닉 크기, 출력값 계산 횟수
hiddenlayer=[]
c = [] # 은닉 층의 각 신경의 입력 개수
p = [] # 은닉 층의 각 신경의 각 입력 데이터 인덱스
w = [] # 은닉 층의 각 신경의 각 가중치
b = [] # 은닉 층의 각 신경의 편향값
W = [] # 출력 층의 각 가중치
B = 0  # 출력 층의 편향값
inputdata=[]
for i in range(m):
  layerinfo = tuple(map(int,input().split()))
  c.append(layerinfo[0])
  p.append([])
  w.append([])
  for j in range(1,c[i]+1):
    p[i].append(layerinfo[j])
  for j in range(1+c[i],c[i]+1+c[i]):
    w[i].append(layerinfo[j])
  b.append(layerinfo[-1])

layerinfo = tuple(map(int,input().split()))
for i in range(m):
  W.append(layerinfo[i])
B = layerinfo[-1]
for i in range(q):
  inputdata.append(tuple(map(int,input().split())))


def hidden(layer):
  output=[]
  for neural_num in range(m):
    temp=b[neural_num]
    for data_num in range(c[neural_num]):
      temp+=(layer[p[neural_num][data_num]-1]*w[neural_num][data_num])
    output.append(temp)
  return tuple(output)

def output(layer):
  temp=B
  for i in range(m):
    temp+=(layer[i]*W[i])
  return temp

for i in range(q):
  print(output(hidden(inputdata[i])))
