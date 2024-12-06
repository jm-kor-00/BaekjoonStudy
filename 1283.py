import sys
import heapq
input = sys.stdin.readline
#거리 초기값 : 무한 inf
INF = float('inf')

def dijkstra(V,graph,S):
    hq = []
    #distance : 시작노드에서 각 노드에 가는데 필요한 비용
    #초기값은 모두 무한
    distance = [INF] * (V+1)
    
    #시작노드까지 거리 : 0
    distance[S] = 0
    #우선순위큐에 삽입
    heapq.heappush(hq,(0,S))
    
    while hq :
        #가장 비용이 작은 걸 꺼냄
        dist, tmpNode = heapq.heappop(hq)
        #이미 처리한 노드라면 continue
        if distance[tmpNode] < dist :
            continue
        #현재 노드에서 갈 수 있는 모든 간선에 대해
        for nxtNode,weight in graph[tmpNode]:
            #nxtNode로 tmpNode를 거쳐서 가는 비용 = cost
            cost = dist + weight
            #cost가 이미 구했던 비용보다 작다면
            if cost < distance[nxtNode]:
                #비용 수정
                distance[nxtNode] = cost
                #우선순위큐에 삽입
                heapq.heappush(hq,(cost,nxtNode))
    #distance배열 반환
    return distance
    
V, E, X = map(int,input().split())

graph = [[]for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int,input().split())
    #graph[u]에는 u에서 갈 수 있는 모든 간선(도착점,비용) 저장
    graph[u].append((v,w))

result = dijkstra(V,graph,X) #result에는 리스트형태로 각 노드까지의 최소비용
for i in range(1,V+1):
    print(result[i] if result[i] != INF else "INF")