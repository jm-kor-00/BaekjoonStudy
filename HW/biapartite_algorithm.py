from collections import deque

#인접 리스트 형식으로 입력받은 그래프를
#BFS를 통해, 이분 그래프인지 판단하는 알고리즘
def biapartite_algorithm(S,N,graph):
    
    visited = [0] * N
    #노드를 방문하면 1 혹은 2로 갱신하여
    #해당노드가 어떤 부분집합에 속하는지 구별
    visited[S] = 1

    queue = deque()
    queue.append((S))

    while queue:
        tmp = queue.popleft()
        # tmp노드와 연결된 노드 중에서
        for node in graph[tmp]:
            #아직 방문안한 노드이면
            if not visited[node] :
                # tmp가 2이면 1로, 1이면 2로 갱신
                visited[node] = visited[tmp] % 2 + 1
                # queue에 node삽입
                queue.append(node)
            #이미 방문한 노드이면
            else :
                #만약 tmp와 같은 그룹이면 즉, 인접한 두 노드가 같은 부분집합이 되면
                if visited[node] == visited[tmp]:
                    #이분그래프 조건 불만족
                    return False
    
    #어떻게 분류되었는지 출력
    groupX = []; groupY = []
    for i in range(N):
        if visited[i] == 1 : groupX.append(i)
        else : groupY.append(i)
    
    print("부분집합 X =",groupX)    
    print("부분집합 Y =",groupY)    
    return True

N = int(input("노드의 개수 입력 : "))
print("그래프(인접리스트) 입력")
graph = []
for i in range(N):
    print(i,":",end=' ')
    graph.append(list(map(int,input().split())))
print("===========================")
if biapartite_algorithm(0,N,graph):
    print("이분그래프가 맞습니다.")
else :
    print("이분그래프가 아닙니다.")