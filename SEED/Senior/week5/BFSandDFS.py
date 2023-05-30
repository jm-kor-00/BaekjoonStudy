from collections import deque

#그래프, 시작노드
def BFS(graph,V):
    N = len(graph) #노드의 개수
    #각 노드 방문여부  나타내는 리스트
    visited = [False] * N

    #시작노드 방문처리
    visited[V] = True

    #큐 생성
    que = deque()
    #큐에 시작노드 삽입
    que.append(V)

    #큐에 요소가 있는동안 반복 = 큐가 비면 탐색 종료임
    while(que):
        #요소(노드) 꺼냄
        tmp = que.popleft()
        #꺼낸 노드 출력(왔다는 뜻)
        print(tmp + 1,end = ' -> ')

        #인접행렬기준
        for i in range(N):
            #i가 인접한 노드이면서 방문하지 않은 노드이면
            if graph[tmp][i] == 1 and not visited[i] :
                #큐에 노드 i 삽입
                que.append(i)
                #노드 i 방문처리
                visited[i] = True



def DFS(graph, V):
    N = len(graph)
    #각 노드 방문여부 나타내는 리스트
    #visited에 삽입된 순서
    visited = [False] * N

    #시작노드 방문처리
    visited[V] = True

    #스택 생성
    stack = deque()
    #스택에 시작노드 삽입
    stack.append(V)

    #스택에 요소가 있는동안 반복 = 스택이 비면 탐색 종료임
    while(stack):
        #요소(노드) 꺼냄
        tmp = stack.pop()
        #꺼낸 노드 출력(왔다는 뜻)
        print(tmp + 1,end = ' -> ')
        
        #인접행렬기준
        #작은 노드부터 보기위해서 큰번호부터 삽입
        #후입선출이기때문
        for i in range(N-1,-1,-1):
            #i가 인접한 노드이면서 방문하지 않은 노드이면
            if graph[tmp][i] == 1 and not visited[i] :
                #스택에 노드 i 삽입
                stack.append(i)
                #노드 i 방문처리
                visited[i] = True

G = [[0,1,0,0,1,0],
     [1,0,1,0,1,0],
     [0,1,0,1,0,0],
     [0,0,1,0,1,1],
     [1,1,0,1,0,0],
     [0,0,0,1,0,1]]

BFS(G,0)
print("\n=================================")
DFS(G,0)