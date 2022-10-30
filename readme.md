### 22/10/30
* 백준-2239(c5) 완료 - 파이썬만 그런 건지는 잘 모르겠으나 시간 제한이 매우 빡빡해 최적화를 극한까지 끌어올려야 겨우 통과할 수 있었다. 백트래킹 문제는 진작에 해결했고 불필요한 자원은 칼같이 배제해야 해결된 점에서 조금 아쉬운 문제이긴 하다.
### 22/10/29
* 백준-9024(bs) 완료 - 간만에 해서 그런지 꽤 난해하게 느껴졌는데, pypy3로만 통과를 할 수 있는 점과 더불어 추후 추가공부를 진행해서 python3로도 통과되는 코드를 작성하면서 다시 익숙해질 수 있도록 연습해야겠다.
### 22/10/28
* 백준-17404(c5) 시도 - 예상치 못한 반례가 있는 듯 하다. 시간을 들여 확인해보자.
* [연등] 백준-17404(c5) 완료 - 문제를 어거지로 풀어서 통과가 안된 것 같다. 갈아 엎고 정석적으로 해결하니 통과되었다.
* [연등] 백준-2239(c5) 시도 - 구현을 어설프게 한 부분을 발견 해 제대로 수정하니 이제 정답은 제대로 나오는 것으로 보인다. 다만 백트래킹 과정에서 비효율적인 부분이 있는지 시간 초과가 발생한다. 점점 정답에 근접해가니 계속 보완해 나가도록 하자!!
### 22/10/27
* 백준-2239(c5) 시도 - 백트래킹이 잘 안 풀린다.. 긴 시간동안 논리를 고민해보자...
* 백준-6603 완료 - 백트래킹을 연습하려고 푼 문제가 의도치 않게 효율적인 조합 라이브러리를 이용하게 되어서 너무 쉽게 풀었다. 앞으로 백트래킹 구현 방법을 잘 숙지해보자.
### 22/10/26
* 백준-1806(c5) 완료 - 투포인터 및 동적계획법(누적 합)을 이용해서 정석적으로 쉽게 풀어냈다.
* [연등] 백준-2239(c5) 시도 - 백트래킹 문제로 생각보다 구현이 어려워 놀랐다. 백트래킹 로직을 잘 구현해보자. [(cf)](https://moz1e.tistory.com/15)
### 22/10/25
* 백준-2166(c5) 완료 - 신발끈 공식만 알면 쉽게 해결할 수 있는 문제였지만 몰랐다면 정말 난해했을 문제였다.
### 22/10/24
* 백준-12852(c5) 완료 - dp를 이용해야 하는 문제처럼 보였지만 시간과 메모리 제한이 넉넉해 단순 BFS로도 쉽게 풀렸다.
### 22/10/23
* 백준-2252(graph) 완료 - 위상 정렬을 처음 구현해본다. 다익스트라처럼 이 코드도 자주 연습하여 쉽고 빠르게 구현할 수 있도록 하자.
* 백준-1005(c5) 완료 - 위상 정렬+DP의 환상적인 콤보였다.. 연습용으론 꽤나 좋은 문제 같다.
### 22/10/22
* 백준-11909(sp) 완료 - 처음엔 다익스트라 문제인 줄 알고 풀었으나 메모리 초과가 떠 일반적인 dp 탐색으로 진행했다. 파이썬 환경에서는 언어 특성 문제로 다익스트라 적용이 불가능 한 것으로 보인다. (dp 풀이도 pypy3 환경에서만 통과할 정도로 파이썬 기준으론 조건이 빡빡하다.)
* 백준-1005(c5) 추가 학습 완료 - 이 문제를 효율적으로 풀기 위해서 위상 정렬을 이용해야 한다. 본문과 예제를 통해 연습하도록 하자. [(본문)](https://sorjfkrh5078.tistory.com/36) [(예제)](https://www.acmicpc.net/problem/2252)
### 22/10/21
* 백준-14284(sp) 완료 - 조금 복잡한 조건의 다익스트라 문제인 줄 알았는데, 문제 설명만 복잡하고 실상은 평범한 다익스트라 기본 문제였다..
* [연등] 백준-1005(c5) 시도 - 처음에 DFS로 구현했다가 시간 초과가 나와 동적 계획법으로 해결을 해야 할 것으로 보인다. 다만 top-down 방식으로 할 지 bottom-up 방식으로 할 지 조금 고민스럽다. 시간을 들여 더 생각해보자.
### 22/10/20
* 백준-17396(sp) 완료 - 양방향 간선 및 간선 제외 처리까지 응용된 문제였다. 개인적으로 큰 어려움은 없었는데 구현 중 실수의 비중이 높은 건지 정답 비율이 생각보다 꽤 낮게 나와있어 놀랐다..
### 22/10/19
* 백준-5972(sp) 완료 - 양방향 간선을 이용한 다익스트라 알고리즘 기본 문제이다. 코드의 형태가 어느정도 외워져 기본 문제는 이제 쉽게 풀리는 것 같다.
### 22/10/18
* 백준-1916(sp) 완료 - 다익스트라 알고리즘을 정교하게 구현해야 해결되는 정석적인 문제였다. 루프가 돌 필요가 없는 부분이나 힙에 집어넣을 필요가 없는 부분들의 특징을 꼼꼼히 잘 숙지하도록 해야겠다.
### 22/10/17
* [연등] 백준-18352(sp) 완료 - 다익스트라 알고리즘을 처음 구현해본다. 아직은 익숙치 않지만 반복 숙달해서 원리와 응용을 이해하고 최단 경로에 대한 심화 알고리즘도 공부해 볼 계획이다.
### 22/10/16
* 백준-17179(bs) 완료 - 케이크를 일정 크기 이상으로 나누는 과정에서 마지막 조각의 길이를 처리하는 부분에 큰 애를 먹었다. 바보같게도 k의 길이 이상으로 n번 자르는게 목표라면 n+1번 잘렸을 때의 경우를 세야 마지막 조각도 조건에 만족한다는 것을 뒤늦게 깨달았다..(마지막에 잘린 두조각을 합쳐진 하나의 조각으로 인식하면 되므로) [(cf)](https://jaekwan.tistory.com/m/147)
### 22/10/15
* 백준-17179(bs) 시도 - 이분 탐색을 진행할 매개 변수의 선정 및 구현이 복잡하여 완료하지 못하였다. 다음에 다시 시도해보자.
* 백준-2805(bs) 완료 - 이분 탐색 문제 풀이의 감을 갑자기 잃은 것 같다. 분명 쉬운 문제인데 갑자기 난해하게 느껴져 해결하는데 다소 시간이 걸렸다.
### 22/10/14
* 백준-18114(bs) 완료 - 1-sum(이분탐색), 2-sum(투포인터), 3-sum(브루트포스+투포인터) 방식으로 pypy3에선 통과했지만 python3 에선 시간 초과 판정을 받아 2-sum과 3-sum 과정을 한번에 합쳐 2-sum(투포인터), 3-sum(투포인터+이분탐색) 방식으로 진행하니 python3에서도 넉넉하게 통과할 수 있었다.
### 22/10/13
* 백준-20444(bs) 완료 - 자른 횟수와 그에 따라 나올 수 있는 색종이의 개수의 경우의 수를 나열하다보니 규칙을 발견하여 그 규칙에 따라 이분 탐색을 진행하니 큰 어려움 없이 해결되었다. 다만 이 문제를 이차방정식과 그래프적 해석을 이용해 푼 사람도 있는 것 같다. [(cf)](https://velog.io/@nnnyeong/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%92%80%EC%9D%B4-%EB%B6%84%EC%84%9D-BOJ-20444-%EC%83%89%EC%A2%85%EC%9D%B4%EC%99%80-%EA%B0%80%EC%9C%84)
### 22/10/12
* 백준-10425(bs) 완료 - 전형적인 이분 탐색 문제로 다이나믹 프로그래밍을 응용하여 해결했다.
* [연등] 백준-23631(bs) 완료 - 구현 자체는 어렵지 않았으나 문제를 이분탐색을 이용하여 해결하는 아이디어 및 그 방법을 떠올리기가 쉽지 않았다. [(cf)](https://lbdiaryl.tistory.com/222)
### 22/10/11
* 백준-11687(bs) 완료 - s1이지만 개인적으로 풀이에 대한 발상이 어렵게 느껴졌던 문제였다. 답을 가정해 놓고 그 답이 입력값에 대한 조건을 만족하는지를 체크하는데, 그 방법이 쉽게 떠오르지 않을 법했다.
### 22/10/10
* 백준-1981(bs) 시도 - 구현은 거의 완성했으나 그 과정에서 사용한 DFS가 너무 오래 걸려 BFS로 구현해야 할 것으로 보이는데 BFS로 경로 추적을 하는 방법을 잘 숙지하지 못해 끝까지 완성은 못하였다.
* 백준-1981(bs) 완료 - 겁먹은 것과 다르게 생각보다 간단한 문제였다. 오래걸리는 DFS 대신 BFS를 쓰는 과정에서 미리 최대값과 최소값을 가정하고 풀어야 답이 훨씬 빠르게 나왔다. (이분탐색으로 차이값 탐색 -> 슬라이딩 윈도우 방법으로 최소값,최소값+차이값 사이 탐색) 다만 반례가 생기지 않도록 꼼꼼하게 처리해 줘야 하긴 했다. 저 최소값과 최대값을 가정하는 과정에서 투포인터도 가능한 것으로도 보인다.
### 22/10/9
* 백준-2110(bs) 완료 - 큰 어려움 없이 풀었다. 오히려 가볍게 적어낸 코드가 반례가 없다는 게 신기할 정도로..
* 백준-1208(bs) 완료 - 이 문제는 이분 탐색이 메인이라기 보단 MIMS(중간에서 만나기)유형이 메인 아이디어인 문제이다. 수열을 반으로 갈라 각각 계산한다음 그 계산된 것 끼리 다시 한 번 계산시켜 답을 내는 구조이다. 그 "다시 한 번의 계산"이 hash, bs, 2 pointer 등의 방법으로 진행시킬 수 있는 것이었다. 따라서 직관적인 MIMS 방법 사용을 포함하여 총 4가지의 풀이를 시도해보았다. 성능상으로는 hash를 이용한 방법이 효율적으로 보인다.[(cf1)](https://hyeo-noo.tistory.com/128)[(cf2)](https://loosie.tistory.com/563)
### 22/10/8
* 백준-3151(bs) 완료 - 몇 시간을 붙들어서 겨우 해결했다.. O(N^2logN)은 (투 포인터로 두 값을 잡고 나머지 목표 값을 이분 탐색) 시간초과가 나는지라 O(N^2)의 해결책을 찾았다. (포인터 i로 값을 순차적으로 잡고, 투 포인터(i+1,n-1)를 돌려 두 포인터의 값의 합에 대한 목표값 찾기) 다만 이 방법도 시간 초과가 나서 두 포인터의 값들이 중복 되어있을 때를 고려해 p2의 움직임을 최소화하도록 하였다. 두 포인터의 값이 같다면 두 포인터의 거리 만큼 답에 더하고 (p1는 중복에 대해 고려하지 않고 진행한다.) 다르다면 p2와 값이 같은 원소의 개수만큼 답에 더한다. (그 개수는 순차탐색이 아닌 이분탐색으로 찾는다. 순차탐색시 시간 초과) 이 외에도 다양한 풀이 방법도 있으며 언어별로 되는 경우도 있고 안되는 경우도 있는 것 같아 꽤 괴랄하게 느껴졌다.. 나중에 다시 한 번 풀어보고 적용시킬 수 있는 알고리즘을 공부해보면 좋을 듯 하다. [(cf)](https://baby-ohgu.tistory.com/32)
* 백준-2467(bs) 완료 - 이분탐색 유형으로 되어있지만 투포인터로 3분만에 매우 쉽게 풀었다. ~~3151번과 같은 난이도 맞나..?~~ 이분탐색으로도 풀어봐야겠다.
* 백준-2467(bs) 추가 학습 완료 - 이분탐색으로 풀어보았다. 다만 투포인터는 O(N), 이분탐색은 O(NlogN)으로 상이한 시간 복잡도를 보임에 따라 정확한 답이 나오더라도 시간복잡도를 고려한 적절한 알고리즘을 찾아야 함을 상기시킬 수 있었다. [(cf)](https://seongonion.tistory.com/100)
### 22/10/7
* 백준-3151(bs) 시도 - 어떤 것을 이진 탐색해야 할 지를 감을 잘 못잡겠다. 계속 고민해보자.
* [연등] 백준-3151(bs) 시도 - 아무리 고민해도 명확한 답안이 떠오르지 않는다.. 일단 쉬운 문제부터 다시 풀어보자.
### 22/10/6
* [연등] 백준-2866(bs) 완료 - 조금씩 유형에 익숙해지고 있는 것 같다. 점점 쉽게 풀린다. 다른 방법으로도 풀 수 있다고 하는데 한번 해보아야겠다.
* [연등] 백준-2866(bs) 추가 학습 시도 - reverse 정렬 후 몇 개가 겹치는지 찾는 방식으로도 한 번 풀어보려다가 구현이 복잡해 완성은 못하였다. 고수의 테크닉은 역시 다른 듯 싶다. [(cf)](https://solved.ac/contribute/2866) 
### 22/10/5
* 백준-16564(bs) 완료 - 역시 비슷한 유형으로 느껴져 탐색을 진행해야 할 변수를 찾아서 반례의 여지없이 코드를 구현하니 쉽게 해결되었다.
* [연등] 백준-2022(bs) 완료 - 제곱근이 포함된 매개변수 이분탐색을 이해하니 생각보다 쉽게 풀 수 있었다!
![2022-3](https://user-images.githubusercontent.com/70588265/194084680-43615360-38ec-4d6a-8b70-c6d4388229bb.png)
### 22/10/4
* 백준-2343(bs) 완료 - 3079번을 풀었던 경험으로 큰 시간 들이지 않고 코드로 옮겼으나 특수한 케이스(원소가 예상 제한 시간보다 계속적으로 큰 경우)에 대해 파악이 늦어져 시간이 오래걸렸다.
### 22/10/3
* 백준-3020(bs) 완료 - 이분탐색을 적절하게 사용해야 할 때를 먼저 고민하고 코드로 옮겨야 할 것 같다. 다른 유형보다도 특히 막 이것도 해보고 저것도 해보는 식으로 접근하면 더 꼬여버리기 쉬운 것 같다. 이점을 앞으로 잘 유념하자. 또한 binary_search를 직접 구현하는 것도 좋지만 bisect 라이브러리를 잘 이용하는 것도 좋을 것 같다.
* 백준-3079(bs) 완료 - 문제를 다양한 관점에서 바라보아야 할 것 같다. 어느 걸 어떤 것을 기준으로 어떻게 찾을지를 잘 고민해보자. 심사대 개수, 사람의 수, 심사시간의 변수 중에서 특정한 심사시간동안 최대의 심사를 받게 했을 때, 그 심사 수가 사람의 수가 되면 해결되는 문제였다. (정확히는 사람의 수 이상이면서 심사시간의 최소) 따라서 심사시간을 이분 탐색하고, 그 과정에서 심사 수를 기준으로 사람의 수와 같거나 큰 지의 여부를 찾는 것이 이 문제의 핵심이다.
* [연등] 백준-2022(bs) 시도 - 수식을 구현하기도 어렵고, 마침내 수식 자체는 찾았지만, 그 방정식을 풀어내는 데에 이분 탐색을 적용시키는 것이 익숙치 않다. 제곱근의 값을 이분 탐색으로 찾아내는 예제에 대해 먼저 학습 및 이해를 한 후 다시 접근해보아야 할 것 같다.
![2022-1](https://user-images.githubusercontent.com/70588265/193604137-38e50cd2-2711-4ace-8dbf-ddacb846810a.png)
![2022-2](https://user-images.githubusercontent.com/70588265/193604157-9ef2a2a3-443a-4380-a3f8-3511f4d6bd6d.png)
### 22/10/2
* 백준-11049(dp) 완료 - dp table도 잘 구성했고 흐름도 잘 구상했지만, 막상 일반화하여 재귀식을 구현하는 것이 잘 안되어서 긴 시간동안 막혔었다..
* [연등] 백준-3020(bs) 시도 - 이분 탐색의 응용 문제를 처음 풀어본다. 생각보다 어떻게 이분 탐색을 적용해야 할 지 생각하는 것이 어렵게 느껴진다..
### 22/10/1
* 백준-1520(dp) 완료 - 이게 왜 될까? dfs에 dp를 어떤식으로 적용시켜야 하는지, 혹은 bfs로는 안되는지, 리턴값이 아닌 dp table에만 접근해서 답을 구해낼 수 있는지 계속 고민해봐야겠다.
* [연등] 백준-1520(dp) 추가 학습 완료 - 1. DFS+DP: 탑다운과 비슷한 방식으로, 우선 처음에 목표지점까지 도달하면 재귀함수를 통해 지나왔던 모든 길에 1을 더한다. 그 후 다른 길로 가던 중 이미 지났던 길을 마주치면, 지나왔던 모든 길에 해당 위치의 dp값만큼 더한다. 이는 dp[x][y]+=dp[nx][ny] 꼴로 일반화 시킬 수 있으며 (처음 가는 길로 목표지점에 도착하면 dp[nx][ny]의 값은 1, 이미 갔던 길에 다다르면 값은 해당 위치의 dp값을 반환.) 지날 수 없는 길과 아직 지나가지 않은 길을 구분하기 위해 dp table을 -1로 초기화 한다. 결국 모든 경우의 수는 출발점인 dp[0][0]에 모여 합산된다. 따라서 함수에서 dp의 값을 리턴하는 것을 이용해서 바로 정답을 출력하게 할 수도 있으며, 그렇지 않고도 모든 탐색이 끝난 후 dp[0][0]을 직접 출력시킬 수도 있는 것이다. 2. BFS+PQ+DP: 바텀업과 비슷한 방식으로, 이 역시 DFS뿐만이 아닌 BFS로도 탐색이 가능하다. 다만 겹쳐지는 길은 중복하여 카운팅 되지 않도록 순서를 조정해야 하는데, 그 이유로 PQ가 사용된다. queue에서 가장 높이가 높은 곳을 우선하여 탐색하도록 한다. (∵그렇지 않으면 탐색 중 경로가 분기되었다가 합쳐져야 할 때, 순서가 어긋나 탐색이 합쳐지지 않을 수 있다.) 분기되고 합쳐지는 것을 반복하며 탐색하면서 이전위치의 값을 현재위치의 값에 계속 업데이트 하여 최종적으로 dp[-1][-1]에 도착하는데, 그 위치에 모든 경우의 수가 합산된다. 이로서 모든 궁금증 해결! [(cf)](https://summa-cum-laude.tistory.com/35)
### 22/9/30
* 백준-5557(dp) 완료 - 쉽게 점화식을 찾았으나, 반례를 막는 과정에서 원인을 생각해내느라 시간이 조금 걸렸다.
* [연등] 백준-1520(dp) 시도 - 문제풀이가 단단히 꼬였다. 논리를 제대로 정립해서 다음에 다시 시도해봐야겠다.
### 22/9/29
* 백준-9084(dp) 시도 - 배낭문제 인 것 같은데 시간이 부족해서 연등 때 이어서 해야겠다.
* [연등] 백준-9084(dp) 완료 - 간만에 배낭 문제 유형을 푸니 처음때처럼 쉽게 감이 안잡히고 안풀렸다. 동전(거스름돈)문제가 dp에서 배낭문제 유형임을 인지하고 for문의 순서에 유의하자. [(dp 응용/심화)](https://letalearns.tistory.com/61)
### 22/9/28
* 백준-2300(dp) 완료 - 드디어 성공했다! 제대로된 점화식을 마침내 찾아내서 쓸데없이 시간을 잡아먹는 코드들을 최적화 시키니 pypy3로 통과할 수 있었다..!
### 22/9/27
* 백준-2631(dp) 완료 - 줄세우기 문제를 이해하자마자 LIS알고리즘의 응용이라는 것을 깨닫고 순식간에 풀었다. g4 문제이지만 풀이 방식을 경험해본 입장이니만큼 쉽게 느껴졌다. [(LIS를 구하는 3가지 알고리즘)](https://dailymapins.tistory.com/84)
* [연등] 백준-2300(dp) 시도 - 이전에 정렬 문제로 풀려다가 높은 수준의 dp 구현이 요구되어서 미뤘던 문제를 다시 풀어봤는데, 긴 시간에 걸쳐 원했던 방식대로 구현은 된 것 같으나 시간 복잡도가 높아 빠르게 돌아가질 않는다. 계속 고민해보자..
### 22/9/26
* 백준-1915(dp) 완료 - dp의 구성이 좀 어렵다. 해당 위치를 정사각형의 오른쪽 아래 꼭짓점으로 하고 위, 왼쪽으로 가는 변의 최대 길이들의 최솟값의 제곱이 정사각형의 넓이가 되는 셈이다. [(cf)](https://suri78.tistory.com/193)
### 22/9/25
* 백준-9252(dp) 완료 - 이전에 LCS를 풀어 본 경험이 있었으나 점화식이 잘 생각이 안났는데, 메모장에 적어보면서 점화식을 유추해내니 예상외로 쉽게 풀렸다! 수열을 구하는 부분은 dp에서 값이 증가하는 부분을 역순으로 추적하여 값을 집어넣으니 해결되었다.
* 백준-10942(dp) 추가 학습 및 최적화 완료 - 다른 풀이를 확인해보니 조금 더 효율적으로 보이는 다른 순서의 바텀업 방식이 있어 적용해보았다. 또한 불필요한 연산을 없애 총 대략 30%의 시간을 단축하였다.
* [연등] 백준-14002(dp) 완료 - 9252번과 비슷한 유형, 표기상 같은 난이도이지만 1차원 dp라 더 쉽게 풀었다.
* [연등] 백준-1915(dp) 시도 - 생각한 점화식이 계속 반례가 나온다. 점화식을 떠올리기가 조금 까다로운 듯 하다.
### 22/9/24
* 백준-11054(dp) 완료 - dp table의 구성, 점화식의 구현에서 어려움을 겪었지만 끝내 통과했다. 모범답안을 보며 제대로 된 풀이를 다시 학습해야겠다.
* 백준-11054(dp) 추가 학습 완료 - 기존에 구현한 방법은 dp 테이블을 증가 수열, 증가+감소 수열로 나눠서 증가는 부분증가수열의 방식으로 구현하였다. 그리고 증가+감소는 해당 인덱스의 수보다 큰 수중 dp table[j][0]이 가장 큰 값을 찾아서, 그 값에 1을 더한 값과 dp[i][0]중에서 큰 값을 넣었다.(∵증가+감소이므로) 그러나 다른 방식을 확인해보니 →방향으로 증가하는 수열, ←방향으로 증가하는 수열의 dp table을 만들어서 각각의 인덱스의 값들의 합 - 1 의 값중 가장 큰 값이 답이 되는 것이었다. 삽질을 한 것 같지만 나만의 새로운 풀이 방식을 만든 것 같아 뿌듯하다.
* 백준-2133(dp) 완료 - 생각보다 점화식을 쉽게 떠올렸다. 기존 타일 채우기의 응용이라 경험이 있어 쉽게 풀은 것 같다. 워낙 점화식이 간단해서 숏코딩도 도전해보았고 81Byte로 10등을 했다!
* [연등] 백준-10942(dp) 완료 - 처음엔 바텀업 방식을 생각했다가 적절한 바텀업 순서를 떠올리지 못해 메모이제이션을 이용한 탑다운(재귀)방식으로 구현했으나, 적절하지 못한 순서 혹은 많은 함수 호출로 인해 시간초과가 발생했다. 때문에 적절한 바텀업 순서를 생각해내어 dp table에 다시 구현하니 시간초과가 발생하지 않고 통과하였다. 타인의 코드도 직접 비교해보면서 최적화에 대해 고민해보아야겠다. [(cf)](https://www.acmicpc.net/status?from_problem=1&problem_id=10942)
### 22/9/23
* [연등] 백준-2011(dp) 완료 - 조건만 조금 까다로운 것 빼고는 큰 어려움 없이 해결했다. 이제 조금 더 어려운 문제를 풀어보자.
* [연등] 백준-11054(dp) 시도 - 어떤 식으로 푸는 문제인지 감은 오는데, 조건이나 분기같은 구현에서 막힌다. 조금 더 고민해보면 풀릴 것 같다!
### 22/9/22
* [연등] 백준-17070(dp) 완료 - 원큐로 성공! bfs나 dfs로도 풀 수 있는 문제로 보이지만 확실히 dp로 푸는 것이 더 직관적이고 적은 시간 복잡도로 해결할 수 있었다.
### 22/9/21
* [연등] 백준-2565(dp) 완료 - 복잡한 문제인줄 알았으나 실상 LIS 문제였다. 전깃줄을 정렬하면 좌측과 우측 모두 오름차순으로 진행되어야 하는데 그렇지 않은 경우는 전깃줄이 꼬인 경우니 가장 잘 오름차순으로 정렬된 것을 제외한 나머지의 개수가 제거해야 할 전깃줄의 개수가 되는 것이다.
* [연등] 백준-2096(dp) 완료 - 매우 전형적인 유형의 문제로 쉽게 풀었다. 또한 메모리 제한이 4MB였는데 2294번을 푼 경험으로 1차원 dp table로 만들어 적은 메모리를 사용해 한번에 통과하였다.
### 22/9/20
* [연등] 백준-2294(dp) 완료 - 처음엔 2차원 dp로 구현하여 O(n^3)의 시간,공간 복잡도를 가졌으나 점화식이 같은 행끼리만 상호작용하므로 굳이 dp table을 2차원으로 만들지 않아도 됐다. 이 부분을 최적화하니 pypy3로만 통과하던 코드가 python3에서도 여유있게 통과하였다.
* [연등] 백준-2565(dp) 시도 - 구현을 괴상하게 해버렸는데, 역시 처음엔 조금 맞는 듯 싶다가 오답이 되었다. 다음 시간에 시간을 갖고 더 고민해보자.
### 22/9/19
* [연등] 백준-2293(dp) 추가 학습 완료 - 2차원 dp로 구현했을 때는 for의 순서가 바뀌어도 문제가 없으나 메모리가 초과되므로 dp를 1차원으로 줄여야 한다. (dp[i][j] = dp[i-coin[j]][j]+dp[i-1][j]) 이 점화식을 1차원으로 바꾸기 위해 dp[i][j]의 값을 dp[i-1][j]의 값으로 간주하고 이 값에 dp[i-coin[j]]를 더해주어야 한다. 다만 이때에는 for의 순서가 바뀌면 안되는게, 하나의 i에 모든 경우의 j를 구해서 한 행을 모두 처리해야 각 행을 업데이트시키면서 처리할 때(과도하게 미리 업데이트 되지 않은) 적절한 값이 들어가 1차원의 dp로 계산할 수 있는 것이다. 2차원 dp를 이해한 후 1차원으로 축소시키는 방식으로 생각하면 그 이유를 쉽게 이해할 수 있다.
* [연등] 백준-2225(dp) 완료 - 점화식을 잘 못세우겠어서 dp table을 그리면서 점화식을 유추해냈는데, g5답지 않게 단순한 점화식으로 굉장히 쉽게 풀렸다. 다음에 왜 점화식이 그렇게 되는지 깊게 이해해 보아야겠다.
### 22/9/18
* 백준-1149(dp) 완료 - 이웃한 집과 다른 색을 칠하면서 모든 집을 칠하는데 드는 비용의 최솟값을 구하는 문제였는데, 배낭 문제로 2차원 dp를 사용해보아서 그런지 쉽게 풀었다.
* 백준-1932(dp) 완료 - s2 풀 때는 어려웠는데 희한하게 s1 문제로 넘어오니 쉽게 느껴진다.
* 백준-2156(dp) 완료 - 점점 쉬워지는 것 같다.
* 백준-9251(dp) 완료 - 처음 LCS 문제를 풀었다. LIS, 배낭 문제와 더불어 대표적인 유형인 것 같은데, 점화식을 잘 숙지할 필요가 있을 것 같다. 최장 공통 연속 부분 문자열, 최장 공통 비연속 부분 문자열 유형을 잘 연습해보자. 처음엔 문자가 같을 때, max(dp[i-1][j],dp[i][j-1])+1 이라고 생각했는데, 단순하게 AAA 와 A를 대입할 때 답이 3이 나오는 반례가 생기므로 잘못된 방식인 걸 깨달았다. [(cf)](https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence)
* [연등] 백준-2293(dp) 완료 - 문제는 풀렸으나 이중 포문의 순서가 바뀌면 잘못되었다는 점에서 의문이 들었다. 또한 dp를 이중 리스트로도 풀어보고자 한다. 다음에 추가학습을 진행해야겠다.
### 22/9/17
* 백준-1535(dp) 완료 - 그 유명한 배낭 문제(냅색) 유형 문제이다. 2차원 dp를 이용해서 처음으로 풀어봐서 그런지 이해가 꽤 어려웠다. 브루트포스: 시간복잡도는 버리고 사용 가능, 그리디: 분할이 가능한 Fractional Knapsack 문제라면 가성비 순으로 정렬해서 가능, DP: 분할이 불가능한 0-1 Knapsack 문제시 사용 가능 [(cf)](https://gsmesie692.tistory.com/113?category=523232)
* 백준-16493(dp) 완료 - 복습차원에서 배낭문제를 다시 한 번 풀어보았다. 한번 풀어본 경험이 있기에 한번에 성공했으나 dp 테이블을 구상하고 점화식을 구현하는 과정에서 조금 생각이 필요하긴 했다.
### 22/9/16
* [연등] 백준-10164(dp) 완료 - dp를 사용하는 알고리즘 자체는 크게 어렵지 않았으나 이를 2차원 매트릭스에서 구현하는 과정에서 조금 어려움을 겪었다. 구현연습을 많이 해보자.
### 22/9/15
* [연등] 백준-15988(dp) 완료 - 점화식은 잘 세웠다. 다만 이를 최적화 시키는 과정에서 나머지 정리를 떠올리지 못해 불필요한 메모리 낭비를 일으켰다. ((A mod n + B mod n) mod n = A+B mod n)
* [연등] 백준-11060(dp) 완료 - 완벽한 점화식, 완벽한 예외처리! 처음으로 한 방에 성공했다.
### 22/9/14
* 백준-1965(dp) 완료 - 문제를 찬찬히 읽어보니 단순한 LIS 문제라 11053번을 풀었던 경험으로 쉽게 풀었다.
### 22/9/13
* [연등] 백준-1699(dp) 완료 - 처음에 18의 제곱수의 개수를 16, 1, 1의 것으로 쪼개서 구하는 식으로 했으나 18은 3^2+3^2여서 3개가 아닌 2개라는 반례가 있어 점화식을 잘 못 세운 것을 확인했다. 다시 생각하니 18보다 작거나 같은 제곱수(16,9,4,1)들을 모두 구한 후 18-16, 18-9, 18-4, 18-1 의 제곱수의 개수들 중 가장 작은 것을 구해서 그것에 1을 더하는 것이 맞는 것을 확인했다. 또한 작거나 같은 제곱수들을 구하는 과정에서도 반복문에 의한 불필요한 시간소모가 있어 리스트 슬라이싱으로 시간 복잡도를 줄이니 결국 통과되었다.
* [연등] 백준-9184(dp) 완료 - 매우 쉽게 풀었다. 문제에서 제시된 재귀함수를 다이나믹 프로그래밍으로 빠르게 최적화 시키는 문제였는데, 점화식도 주어져 있어 큰 생각 없이 풀었는데도 간단히 풀었다. 내가 약한 부분은 역시 점화식 세우는 부분인 것 같다.
### 22/9/12
* 백준-11053(dp) 완료 - 다이나믹 프로그래밍의 대표 유형인 LIS 문제였다. 부분 수열은 전체 수열에서 일부 항을 없애서 만드는 수열이라 이해하면 좋다. 상향식으로 문제를 푸는데, dp[i]를 결정하기 위해선 j로 dp[0]~dp[i-1] 까지 훑어서 arr[j]가 arr[i]보다 값이 작으며(∵증가하는 수열이므로), 그것을 만족하는 j값들 중에서 dp[j]값이 가장 큰 j를 고르면 된다. 그때의 j값이 dp[i]=dp[j]+1 을 만족한다.
* 백준-1912(dp) 완료 - dp에 들어가는 값이 해당 수열 내에서 만들 수 있는 최대의 합이 아니다. 더할지, 안더하고 합을 새로 시작할지를 결정해야 하는데, 이 값을 이전값에 더하는 것과, 현재 인덱스값 중 큰 값을 dp테이블에 넣고 점화시켜야 한다. 대표유형들을 풀고 있는 만큼 풀었던 dp 문제들은 다음에도 다시 한 번 풀어보자..
### 22/9/11
* 주말 외출로 할 시간이 없었다. 연등 시간에 이어서 해야겠다!
* [연등] 8-4(dp) 완료 - 점화식을 생각해내는 것이 좀 어려웠다.
* [연등] 8-5(dp) 완료 - 점화식만 떠올리면 끝나는건데.. 잘 안떠오른다.
* [연등] 11053(dp) 시도 - 문제 이해도 잘 안되고 점화식을 어떻게 만들 수 있는지도 잘 안떠오른다...
### 22/9/10
* 8-2(dp) 완료 - 어느정도 감이 잡힌다.
* 8-3(dp) 완료 - 점화식이 슬슬 바로 생각난다.
### 22/9/9
* 백준-2300(sort) 시도 - 1차원 기지국 문제도 많이 어려웠는데, 2차원 기지국 문제라 더더욱 어렵게 느껴진다. 다이나믹 프로그래밍에 대해 더 익숙해질 필요가 있을 것 같다.
* [연등] 2300번의 문제가 다이나믹 프로그래밍의 성격이 짙어 디렉토리를 변경하였다.
* [연등] 8-2(dp) 시도 - 점화식을 이용한 동적 프로그래밍이 아직은 낯설다..
### 22/9/8
* 백준-25341(implementation) 완료 - 시간복잡도를 줄이는 데에 성공했다! 은닉층에 있는 뉴런에 하나하나 입력값을 넣으면 2000*2000의 연산이 있으므로 이를 생략해 은닉층에 출력층을 먼저 합친다. 그리고 은닉층에 있는 입력인덱스 값에 대응되는 가중치 값을 모두 확인해서 입력 인덱스 값에 대한 dict로 각 입력에 대해 곱해야 할 최종 값을 만들어낸다. 그렇게 되면 2000의 연산으로(=입력층에만 대한 연산) 수행해낼 수 있다.
### 22/9/7
* 외출로 할 시간이 없었다ㅠ
### 22/9/6
* 백준-25341(implementation) 시도 - 아무리 생각해도 감이 안 잡힌다. 계속 고민해봐야겠다. [(cf)](https://junseok.tistory.com/264)
### 22/9/5
* 격리 해제! 그러나..
* 백준-25341(implementation) 시도 - 시간복잡도가 잘 안줄어든다. 2000(q) * 2000(m) * 2000(c) 의 계산을 어떻게 줄일 수 있을까?
### 22/9/4
* 격리 5일차. 공부하고싶다.
### 22/9/3
* 격리 4일차.
### 22/9/2
* 격리 3일차.
### 22/9/1
* 격리 2일차.
### 22/8/31
* 확진자 밀접접촉자로 분류되어 격리..
### 22/8/30
* 백준-25341(implementation) 시도 - 기존에 인공 신경망의 구조를 알고 있었기 때문에 구현은 빠르게 되었지만, 시간 복잡도에서 걸렸다. 계산을 간소화 하여 시간 복잡도를 줄여보자. > (ax+b)*c+d = acx+bc+d
### 22/8/29
* 개인정비시간 부족으로 하루 휴식.
### 22/8/28
* 백준-1826(sort) 완료 - 현재 위치에서 도달 가능한 모든 주유소를 heap에 push. 그 후 가장 연료를 많이 주는 주유소에서 주유. (이때 현 위치보다 앞에 있는 주유소일 경우 pos 를 그 주유소 위치로 만들고 그 거리만큼 연료에 마이너스. ∵ 한번 주유를 했음에도 불구하고 다음 주유소 혹은 목적지까지 도달이 불가능할 경우 지나쳤던 주유소에서 주유를 하게 될 수도 있으므로) 이때 주유할 수 있는 주유소가 heap에 하나도 없는 경우 -1 출력하고 종료. [(cf)](https://fre2-dom.tistory.com/59)
### 22/8/27
* 백준-1826(sort) 시도 - 잘못된 그리디 알고리즘을 사용해서 문제가 발생했다. [(cf)](https://velog.io/@sunjoo9912/%EB%B0%B1%EC%A4%80-1826-%EC%97%B0%EB%A3%8C-%EC%B1%84%EC%9A%B0%EA%B8%B0) -> 현재까지 지나쳐온 주유소를 체크하는게 핵심이다. 연료가 부족하면 지금까지 지나쳐온 주유소중 가장 연료가 많았던 주유소의 연료량만큼 채우고 count+=1 하면 된다.
* [연등] 백준-1826(sort) 시도 - maxheap을 사용하여 구현했으나 구현실력이 아직 낮아 통과를 못하고 있다. [(cf)](https://travelbeeee.tistory.com/492)
### 22/8/26
* 백준-2457(sort) 시도 - 시간이 없어서 구현을 많이 못했다. 연등이나 다음날에 이어서 해보자.
* [연등] 백준-2457(sort) 완료 - 여러 엣지케이스를 하나하나 열심히 막아주었더니 성공했다. ~~그 대신 코드는 이렇게 푸는게 맞나 싶을 정도로 더러워졌다~~
* readme 날짜 내림차순으로 재정렬
### 22/8/25
* [연등] 백준-10800(sort) 완료 - 같은 크기, 다른 색의 공일 때 공의 개수를 카운트하는 로직은 단순히 각 공의 개수의 합을 1씩 제거함으로써 잘못된 누적합 계산을 해결했다. 그리고 hash를 적극 이용하자. 불필요한 이중 리스트는 hash의 키로 tuple을 사용하면 빠르고 가볍게 돌릴 수 있다. dict와 set을 손에 잘 익히자. 
### 22/8/24
* 이하 동일
### 22/8/23
* 사지방이 휴게공간으로 바뀌어 며칠간 이용을 못하게 되었다.
### 22/8/22
* 오늘은 휴식. 많이 바빴고 시간이 없었다.
### 22/8/21
* 백준-2473(sort) 최적화 - pypy3는 정말 빠르게 푸는데, python3 는 아슬아슬하게 시간 초과가 난다. 구글링해서 성공한 코드와 같은 알고리즘으로 만들어도 왜 내 경우는 시간초과인지 잘 모르겠다. 패스..
* 백준-13904(sort) 완료 - 깊이 생각하니 풀 수 있었다. 조금 특이한 방법으로 풀은 것 같긴 한데, 정석을 참고해보아야겠다.
* 백준-13904(sort) 추가 학습 완료 - 조금 더 정석에 가까운 알고리즘으로 다시 해결했다.
* 백준-2109(sort) 완료 - 13904와 큰 차이가 없는 문제였다.
* [연등] 백준-10800(sort) 시도 - 같은 크기, 다른 색의 공일 때 공의 개수를 카운트하는 로직에서 시간이 부족하여 완료하지 못했다. 다음 시간에 성공시켜야겠다.
### 22/8/20
* 백준-3649(sort) 완료 - 역시 큰 어려움 없이 풀었다. 문제에 테스트 케이스가 여러개였다는 것이 함정;
* 백준-14921(sort) 완료 - 투 포인터 정복. (정렬되어있다는 가정 하 / 차의 최소 : -> ->, 합의 최소 : -> <-, 합 혹은 차의 값 찾기 : 둘 다 가능하긴 함)
* 백준-5052(sort) 완료 - g4인데도 불구하고 매우 쉽게 풀었다..
* [연등] 백준-2473(sort) 완료 - 이것도 g3치고 pypy3로는 쉽게 풀렸으나, python3 로는 시간초과가 난다. 가장 이상적인 시간 복잡도(=O(N^2))로 처리한 것 같은데, 아무리 최적화해도 쉽게 해결되지 않았다.. 다음에도 계속 최적화 해보자.
### 22/8/19
* 백준-1744(sort) 완료 - 큰 어려움 없이 풀었으나, 논리의 허점 및 반례를 생각해보는 연습이 필요할 것 같다.
* [연등] 백준-2170(sort) 완료 - 비효율적인 탐색이 있다면(순차탐색 등) 정렬의 이점을 활용해 시간 복잡도를 줄이자. 또 정렬 후의 특성을 이용해 논리를 잘 구성해 해결하자.
* [연등] 백준-2230(sort) 완료 - 투 포인터의 여러 활용 방법을 익히자. (-> <- , -> ->)
### 22/8/18
* 백준-2208(bfs) 완료 - 벽을 뚫고 방문한 경우와 벽을 뚫지 않고 방문한 경우를 나눠서 한 리스트에 0,1,2 로 구분했는데, 그러니 충돌 자체는 안나서 답은 올바르게 나오지만 불필요한 큐가 계속 생겨 시간 복잡도를 늘렸다. 따라서 각 경우의 방문 리스트를 두개로 만들어서 처리하니 잘 통과되었다.
* [연등] 백준-2470(sort) 완료 - 처음엔 어떻게 풀어야 하나 난감했는데, 정렬된 리스트를 기반으로 투 포인터를 이용해 비교하니 쉽고 빠르게 풀렸다!
### 22/8/17
* 1987번은 충분히 학습한 것 같으니 다음 문제를 풀어보자.
* 백준-2206(bfs) 시도 - 벽을 뚫고 방문한 경우와 벽을 뚫지 않고 방문한 경우가 충돌하는데, 이를 해결할 시간이 부족하다. 다음에 계속 방법을 고민해보자.
### 22/8/16
* 오늘은 내 생일이다. 근데도 아직 격리구나.
### 22/8/15
* 코로나 유증상으로 격리돼서 사지방을 이용할 수 없어 코딩 연습을 하지 못했다..
### 22/8/14
* 백준-1987(dfs) 시도 - 와.. 몇시간을 붙들어도 안풀린다. python3는 시간초과, pypy3는 메모리 초과.. 메모리를 희생해 계속 시간 최적화를 해보아도 파이썬에서 시간초과가 뜬다. 계속 붙들고 답까지 가보자.
* [연등] 백준-1987(dfs) 완료 - setrecursionlimit의 크기만큼 메모리를 미리 잡아먹는다는 사실을 간과했다. 그 값을 줄이니 pypy3에서 메모리초과가 안뜨고 성공했다. 계속 최적화시켜서 python3로도 빠르게 돌아가도록 해보아야겠다.
* [연등] 백준-1987(dfs/bfs) 최적화 완료 - DFS, BFS 모두로도 풀 수 있었으며 최종적으로 bfs로 python3에서 성공했다. ★ 그보다 정말 중요한건, set이 굉장히 빠른 자료형이라는 것이다. BFS로 풀었을때에도 오래걸린 이유가 중복된 작업이 계속 큐에 들어가서 진행되었기 때문인데, 큐로서 set을 사용하면 랜덤으로 큐에서 나온다는 것만 제외하면 (큐에서 나오는 순서가 중요하지 않다면) hash를 사용하는 set 특성상 O(1)의 속도로 중복여부를 체크해서 불필요한 중복작업의 push/pop을 막아주고, 나머지는 deque와 동일하게 push 및 pop 도 O(1)로 빠르게 처리 가능하다. 정리: BFS+큐 순서X+중복큐 제거 -> set() ★
* [연등] 백준-1987(dfs/bfs) 추가 공부 - 특이하게, set을 이용해서 python3에서 2초 가량 걸리던 코드가 pypy3에선 9초 이상의 시간이 걸려 시간초과가 난다. 그리고 set의 사용 조건에서 큐의 순환을 카운팅하지 않아야한다는 조건이 있어야 한다고 적었는데 그건 아니었다. ex) while Q: ... count+=1 for _ in range(len(Q)): ...  도 가능. 그리고 deque로 set의 기능을 구현해서 중복작업을 O(1)로 안하게 만들면서 들어간 순서대로 큐가 나오게 시도해보고 있다. 시간이 없어서 다음에 해보자.
### 22/8/13
* 백준-14502(dfs) 완료 - 문제 조건을 잘 못 이해해서 삽질했다. 쓸데없었던 부분을 없애고 코드 보완해주니 의외로 쉽게 통과했다.
* 백준-1987(dfs) 시도 - 문제가 간단한 건줄 알았는데 의외로 시간복잡도에서 난관에 부딪혔다. 관련 알고리즘으로 백트래킹이 있는데 생소한 개념인만큼 공부해서 다시 풀어보도록 하자.
### 22/8/12
* 백준-2668(dfs) 완료 - 그래프에서의 loop를 찾는 것이 핵심이었다. 짜면서도 이게 맞는건가 싶었지만.. 그래프 이론을 코드로 표현하는 방법을 잘 이해해보아야 겠다.)
* [연등] 백준-6593(bfs) 완료 - 매우 간단한 bfs 문제라 쉽게 풀었다. 근데 귀찮은 조건문이 코드를 길고 가독성 낮게 만들었다..
* [연등] 백준-14502(bfs/dfs) 시도 - 난이도가 역시 gold4 여서 그런지 구현이 좀 복잡한 것 같다. 시간이 부족하니 다음에 계속 이어서 해보자.
### 22/8/11
* 백준-2251(bfs) 완료 - 방문 처리를 인덱스 접근 방식이 아닌 if ~ in 체크로 했는데도 시간초과는 커녕 매우 빠르게 통과됐다! 문제 조건이 살짝 난해하긴 했지만, 이해하니 쉽게 해결했다.
### 22/8/10
* 백준-16928(bfs) 완료 - 굉장히 쉽고 빠르고 정확하게 풀었다. bfs를 열심히 푼 성과가 보이는 것 같다!
* [연등] 백준-13023(dfs) 완료 - 그래프 탐색은 무작위 루프 탐색이 아닌 list[a] = b 방식으로 표현하면 훨씬 시간 복잡도를 줄일 수 있다! 잘 기억하자.
* [연등] 백준-2251(bfs/dfs) 시도 - 계산식이 조금 헷갈린다. 시간적 여유를 두고 다음에 다시 풀어보자.
### 22/8/9
* 백준-1068(bfs) 완료 - 문제를 완전히 잘못 이해하고 있었다. 이진 트리도 아닌데.. 제대로 이해하고 나니 쉽고 빠르게 풀 수 있었다. 풀기는 bfs로 풀었지만 충분히 dfs로도 풀 수 있을 것 같다. 그리고 새로운 트리 표현 방식을 알게 되었다. 조금 복잡하긴 하지만 잘 유념하고 있어야겠다.
### 22/8/8
* 백준-1068(bfs) 시도 - 트리가 왜 갑자기 어렵게 느껴질까.. 이론은 잘 알고 있는데 응용이 잘 안된다.
### 22/8/7
* 백준-5014(bfs) 완료 - 리스트 길이를 늘리니 해결..
* 백준-2589(bfs) 완료 - 삽질을 좀 했지만 해결. "방문 처리는 큐에서 꺼낼 때가 아니라 큐에 넣을 때!!"
### 22/8/6
* 백준-16234(bfs/dfs) 완료 - pypy3는 통과, python3 는 50ms 차이로 성공했는데, bfs로 푸는게 효율적인 문제를 dfs로 풀어서 그런 것 같다..
* [연등] 백준-2468(dfs) 완료 - 단순한 dfs문제로 쉽게 풀었다.
* [연등] 백준-5014(bfs) 시도 - 이상한 인덱스 에러가 뜬다. 시간이 없으니 원인 찾기와 해결은 내일 해보자..
### 22/8/5
* 오늘은 즐겁게 놀고 먹은 날! 공부도 하루 휴업~
### 22/8/4
* 백준-10026(dfs/bfs) 시도 - 시간이 없어서 진행을 못했다. 연등 때 이어서 해보아야겠다.
* [연등] 백준-10026(bfs) 완료 - 어려운 건 딱히 없었는데 재귀 깊이 설정 때문에 혹시 틀렸나 걱정했다. sys.setrecursionlimit(n) 을 잘 기억하자.
* [연등] 백준-7569(bfs) 완료 - 7576의 3차원 버전이다. 기존 코드 수정해서 빠르고 쉽게 해결했다!
* [연등] 백준-16234(bfs/dfs) 시도 - 문제 조건이 다소 복잡하여 구현하는데 시간이 부족했다. 그룹을 짜는 건 완료했지만 그 후 이동시간을 계산하는 건 다음에 다시 시도해 보아야겠다..
### 22/8/3
* 백준-7576(bfs) 완료 - deque의 queue를 사용하니 쓸데 없는 루프가 사라져 시간복잡도가 많이 줄어서 성공했다. bfs의 핵심을 잘 기억하자..
### 22/8/2
* [연등] 백준-7576(bfs) 시도 - 시간복잡도가 매우 큰 듯 하다. bfs이니 deque의 queue를 사용해서 최적화를 해보자..
### 22/8/1
* [연등] 백준-14503(implementation) 완료 - 조건이 구체적으로 나와있어 구현하기에 쉬웠다.
* [연등] 백준-2667(dfs) 완료 - 간만에 해보는 dfs이지만 생각만큼 어렵지 않았다.! 다음엔 바로 골드 풀어도 될 듯
### 22/7/31
* 백준-16926(implementation) 최적화 완료 - rotate를 이용하여 swap 및 회전의 반복을 줄이니 시간 복잡도가 상당량 줄어들었다. 회전시킬 테두리를 일차원 리스트로 만들어서 rotate 시키는게 핵심.
* 백준-2564(implementation) 완료 - 삽질을 너무 많이 했다.. 근데 내가 했던 것 처럼 테두리를 일자로 펴서 구하는 아이디어는 흔치 않은 듯??
### 22/7/30
* 백준-16926(implementation) 완료 - 구현 문제에 많이 약한 것 같다. 돌이켜보면 그렇게 어려운 로직은 아닌데, 시간복잡도를 줄이는 데에 시간을 많이 허비했다. 연등시간에 시간복잡도를 더 줄여봐야겠다. 5초 제한 시간인데 4.956초로 해결했다..
* [연등] 백준-13335(implementation) 완료 - 생각보다 어렵지 않게(?) 해결한 것 같다. 문법에서 조금 삽질을 했으니 이부분만 보완을 하면 될 듯..
* [연등] 백준-16926(implementation) 최적화 시도 - 시간복잡도를 거의 못줄였다. 다음번엔 queue 의 rotate 메소드를 이용해봐야겠다..
### 22/7/29
* [휴가] 휴가 복귀했다.. 연등 할 수 있으면 그 때 마저 2504번을 해결해 보아야겠다.
* [연등] 백준-2504(implementation) 완료 - 역대급으로 복잡했던(?) 문제였다.. stack 사용으로 시간 복잡도를 줄이고, 타입 검사등으로 스택에 덧셈 곱셈 숫자 정보를 잘 푸쉬하고 여러 경우의 수를 고려해 값을 정리하는 테크닉이 좀 필요하다. 꼭 다음에 다시 한 번 풀어봐야지..
### 22/7/28
* [휴가] 휴식
### 22/7/27
* [휴가] 백준-2504(implementation) 시도 - 좀 어렵다..
### 22/7/26
* [휴가] 백준-2504(implementation) 시도 - 답 자체는 잘 나오지만 시간 복잡도가 큰 것 같다. 다음에는 스택을 활용해보자.
### 22/7/25
* [휴가] 백준-2504(implementation) 시도 - 이산수학 시간에 배웠던 것 같은데 조금 가물가물 한 것 같다. 복습을 해보아야겠다.
### 22/7/24
* 휴가 준비로 인해 바빠서 개인정비 시간동안 풀지 못했다.. 내일은 기다리던 첫 휴가
* [연등] 백준-2615(implementation) 완료 - 조건이 다양하다보니 사소한 잔실수가 너무 많다. 디버깅 확실히 하자..
* [연등] 백준-1713(implementation) 완료 - EZ
* [백준 코테 단골 유형 실버 문제집](https://www.philgineer.com/2021/11/codingtest-selection.html)
* [연등] 백준-10997(implementation) 완료 - 규칙만 잘 찾으면 큰 어려움 없이 풀 수 있었다.
### 22/7/23
* 백준-15686(implementation) 시도 - 정확한 구현을 못하겠다. 실력을 많이 쌓고 다음 기회에 재도전 하자..
* [연등] 백준-1138(implementation) 완료 - itertools의 사용법만 잘 알면 쉽게 풀 수 있다.
* [연등] 백준-2615(implementation) 시도 - 꽤 조건이 복잡한 것 같다. 시간이 부족하므로.. 다음에 else 부분 부터 수정 들어가자.
### 22/7/22
* 백준-18111(implementation) 시도 - 시간이 없어서 마무리를 못했다. 연등때 마무리 하기로!
* (22/7/20 에 "백준-15686(implementation)"이 "백준-15686(greedy)"로 잘못 적혀있어 수정)
* [연등] 백준-18111(implementation) 시도 - 문제 접근 방법을 잘 모르겠다. 다음에 다시 해보자.
* [연등] 백준-10773(implementation) 완료
* [연등] 백준-18111(implementation) 완료 - 잔 실수가 굉장히 많았다. 코드를 확실하게 짜자..
### 22/7/21
* 오늘 신병이 들어와서 너무 바빴다. 정신 읎서..
### 22/7/20
* [연등] 백준-15686(implementation) 시도 - 논리를 제대로 생각하지 않고 무작정 풀려고 한게 문제인 것 같다. 좀 더 간단한 논리를 차근차근 생각해보고 코드로 옮겨보자.
### 22/7/19
* 백준-1083(greedy) 완료 - 문제의 조건을 너무 어렵게 생각했다. 논리를 꼼꼼하게 정리하여 어떤 조건을 걸어야 하는지 차분하게 생각해보자.
* [연등] 백준-19940(greedy) 완료 - 상황 별 진행 순서를 명확하고 체계적으로 짜자. 루프돌며 1씩 더하거나 빼는게 아닌 몫계산으로 시간복잡도를 낮춤.
* 다음 계획: 내일부턴 구현(implementation) 연습을 해보자.
### 22/7/18
* 야간 사격 훈련으로 인해 할 시간이 없다.
### 22/7/17
* 백준-1461(greedy) 완료 - 조건이 의외로 까다로워 구현에 애를 먹었다. 일반화를 더 꼼꼼히 하고 반례를 열심히 찾자.
* 백준-13164(greedy) 완료 - 열심히 푼 성과가 보인다. 내용은 다르지만 2212번과 요구하는 사항이 동일하다는 걸 깨닫고 바로 풀었다!
* 백준-19539(greedy) 완료 - 아이디어를 생각하기 어려운 문제였다. 나중에 다시 한 번 깊게 생각해보자.
* 백준-11509(greedy) 완료 - 시간복잡도를 낮추는 방안을 여러가지 생각해보자. (heap 등도 있지만 한개 한개의 절차 대신 연속으로 진행시키는 시도 -> 시간복잡도의 차수가 낮아진다.)
* [연등] 백준-1374(greedy) 완료 - 11000과 동일한 문제다
* [연등] 백준-1083(greedy) 시도 - 루프 조건이 좀 까다로우니 신경써서 해보자.
### 22/7/16
* 백준-11000(greedy) 완료 - heap 응용을 통한 시간 복잡도 낮추기.
* (22/7/14의 1946은 import sys ; sys.stdin.readline() 이 핵심)
* 백준-2212(greedy) 완료 - 확률과 통계 문제처럼 전체구간에서 필요없는 구간의 최대값을 이용하여 필요한 구간의 최소값을 구하는 테크닉 이용. (≒여집합?)
* 백준-12904(greedy) 완료 - 제시된 대로가 아닌, 생각을 뒤집는 발상의 전환 필요
* 백준-1041(greedy) 완료 - 일반화만 잘하면 의외로 쉽다.
* 백준-1092(greedy) 시도 - 시간 복잡도를 줄이는 노력을 해보자.
* [연등]백준-1092(greedy) 완료 - 정렬된 데이터에서 무의미한 검색을 줄이는게 핵심!
* [연등]백준-1461(greedy) 시도 - 구현이 복잡하여 일부 예제에서 오답이 나온다. 다음시간에 꼼꼼하게 체크하자!
### 22/7/15
* 백준-11000(greedy) 시도
* 골드 아니랄까봐 난이도가 갑자기 어려워졌다. 시간 복잡도를 줄이는 노력을 해보자.
### 22/7/14
* 백준-2839(greedy) 완료
* [연등] 백준-11399(greedy), 백준-11047(greedy), 백준-1931(greedy), 백준-1946(greedy) 완료
### 22/7/13
* DFS/BFS 학습 시작  (5-3 음료수 얼려 먹기까지 완료)
* 연등으로 추가 학습 시작(DFS/BFS 학습 완료)
* 다음 계획: https://www.acmicpc.net/problem/tags 에서 greedy, implementation, DFS/BFS 복습하기
### 22/7/12
* DFS/BFS 및 인접 행렬, 인접 리스트 등 그래프 관련 이론 학습 완료
### 22/7/11
* 구현(implementation) 학습 시작(4-3 왕실의 나이트까지 완료)
* 연등으로 추가 학습 시작(implementation 학습 완료)
### 22/7/10
* replit 연동 후 '이것이 취업을 위한 코딩테스트다 with 파이썬'으로 학습 시작
* greedy 학습 완료
