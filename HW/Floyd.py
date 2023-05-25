INF = float('inf')

#인접행렬로 나타낸 그래프
# adj = [[0,7,0,0,3,10,0],
#         [7,0,4,10,2,6,0],
#         [0,4,0,2,0,0,0],
#         [0,10,2,0,11,9,4],
#         [3,2,0,11,0,13,5],
#         [10,6,0,9,13,0,0],
#         [0,0,0,4,5,0,0]]
adj = [[0,7,0,0,3,10,0],
        [7,0,4,10,2,6,0],
        [0,4,0,2,0,0,0],
        [0,10,2,0,11,9,0],
        [3,2,0,11,0,13,0],
        [10,6,0,9,13,0,0],
        [0,0,0,0,0,0,0]]

n = len(adj[0]) #그래프의 크기
char_node = [chr(65+i) for i in range(n)] #노드번호를 문자로 변경
dist = [[INF for _ in range(n)]for _ in range(n)] #가중치 나타낼할 배열
path = [[i for i in range(n)]for _ in range(n)] #경로에서 거치는 노드를 저장할 배열
#path[a][b]의 초기값은 b

#인접행렬 출력함수
def print_graph(graph):
    print("=================================")
    for row in graph :
        for el in row :
            if el != INF :
                print("%4d"%el,end='')
            else : print(" INF",end='')
        print()
    print("=================================")

#경로추적 함수
def follow_path(path, S, E):
    global char_node
    if path[S][E] != E:
        follow_path(path, S, path[S][E])
        print(char_node[path[S][E]],end=" -> ")
        follow_path(path, path[S][E], E)

#main문
#가중치그래프에서 현재 알수없는 값을 INF로 수정
for i in range(n):
    for j in range(n):
        if i == j : 
            dist[i][j] = 0
        elif adj[i][j] != 0:
           dist[i][j] = adj[i][j]
        else :
            dist[i][j] = INF

print("=================================")
print("Initial Weight")
print_graph(dist) #플로이드 알고리즘 수행 전 가중치

#플로이드 알고리즘
for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            if dist[i][j] > dist[i][k] + dist[k][j] :
                dist[i][j] = dist[i][k] + dist[k][j]
                path[i][j] = k #경로가 갱신되면 path배열의 값도 수정

print("Floyd Result")
print_graph(dist) #플로이드 알고리즘 수행 후 가중치

#S번 노드에서 나머지 노드로 가는 최소비용경로출력과정
S = 0 #시작노드의 번호
print("Shortest Path from ["+char_node[S]+"]")
print("=================================")

for i in range(n):
    if i == S : continue #시작노드와 같으면 생략 
    print("["+char_node[S]+" -> "+char_node[i]+"] : ",end='')
    print(char_node[S],end=" -> ")
    if dist[S][i] == INF: #도달할 수 없는 노드인 경우
        print("["+char_node[i]+"]에 도달 불가능")
    else :
        follow_path(path, S, i)  # 노드S 에서 i번 노드로 가는 경로
        print(char_node[i])
print()