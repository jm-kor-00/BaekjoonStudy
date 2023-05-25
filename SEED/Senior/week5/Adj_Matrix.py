def print_adjMatrix(graph):
    print("==========================")
    for row in graph:
        for el in row:
            print(el,end=' ')
        print()
    print("==========================")

#인접행렬로 표현
#그래프 형태는 PDF참고
#노드번호 1~6 => 인덱스 0~5 로 대치함

#case1 : 행렬(2차원배열)로 표현
G = [[0,1,0,0,1,0],
     [1,0,1,0,1,0],
     [0,1,0,1,0,0],
     [0,0,1,0,1,1],
     [1,1,0,1,0,0],
     [0,0,0,1,0,1]]

print_adjMatrix(G)

#case2 : 입력받기

N = 6 #노드의 개수
#N x N 행렬생성
Graph = [[0 for _ in range(N)]for _ in range(N)]

#간선 입력받기
for _ in range(int(input('간선의 개수 : '))):
    u, v = map(int,input('인접한 두 정점 입력 ex) 1 2 : ').split())
    u -= 1; v -= 1 #노드번호 맞추기 위해서 -1
    # (u,v) & (v,u) 를 1로 초기화
    Graph[u][v] = 1
    Graph[v][u] = 1

print_adjMatrix(Graph)