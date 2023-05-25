import copy

def printD(D):
    vsize = len(D)
    for i in range(vsize):
        for j in range(vsize):
            if(D[i][j] == INF) : print(" INF ", end='')
            else: print("%4d "%D[i][j], end='')
        print("")
        #print("  #", vertex[i])
    print("===================================")

def print_path(K):
    global vsize
    for j in range(1, vsize):
        print(vertex[0], "-->", vertex[j] ,": ", end='')
        if (K[0][j] <= 0):
            print("경로 없음")
        else:
            print(vertex[0], "-> ",end='')
            path(K, 0, j)
            print(vertex[j], "-> ",end='')
            print("최단 경로")
            
def path(P, u, v):
    if P[u][v] != v:
        path(P, u, P[u][v])
        print(vertex[P[u][v]], end=' -> ')
        #수정
        #path(P, P[u][v],u)였음 ㄷㅈ?
        path(P, P[u][v], v)

def shortest_path_floyd(vertex, W):
    vsize = len(vertex)
    D = copy.deepcopy(W)
    #수정
    #초기값이 0이 아니라 각 배열의 목적지로함 ex) [0][a] 이면 초기값a
    K_list = [list(d for d in range(vsize)) for _ in range(vsize)]

    printD(D)
    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if(D[i][k] + D[k][j] < D[i][j]):
                    D[i][j] = D[i][k] + D[k][j]
                    K_list[i][j] = k
    printD(D)
    for i in range(vsize):
            for j in range(vsize):
                print(K_list[i][j], end=' ')
            print("")
    print_path(K_list)
        
INF = 9999  #거리가 무한대
vertex = ['A','B','C','D','E','F', 'G']
vsize = len(vertex)

weight = [[0,7,INF,INF,3,10,INF],   # 0은 자기 자신, INF는 간선 없음
        [7,0,4,10,2,6,INF],
        [INF,4,0,2,INF,INF,INF],
        [INF,10,2,0,11,9,4],
        [3,2,INF,11,0,13,5],
        [10,6,INF,9,13,0,INF],
        [INF,INF,INF,4,5,INF,0]]
"""
weight = [[0,50,45,20,35,INF],  
        [25,0,10,15,20,INF],
        [INF,INF,0,INF,30,INF],
        [10,60,51,0,15,INF],
        [INF,INF,36,INF,0,INF],
        [INF,INF,39,INF,3,0]]
"""
print("Shortest Path By Floyd's Algorithm")
shortest_path_floyd(vertex, weight)