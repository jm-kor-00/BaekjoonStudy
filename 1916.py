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

    #시작노드까지 거리 = 0
    distance[S] = 0
    #우선순위큐에 삽입
    heapq.heappush(hq,(0,S))
    
    while hq :
        #가장 비용이 작은 걸 꺼냄
        dist, tmp = heapq.heappop(hq)
        #이미 처리한 노드라면 continue
        if distance[tmp] < dist :
            continue
        #현재 노드에서 갈 수 있는 모든 간선에 대해
        for next,weight in graph[tmp]:
            #nxtNode로 tmpNode를 거쳐서 가는 비용 = cost
            cost = dist + weight
            #cost가 이미 구했던 비용보다 작다면
            if cost < distance[next]:
                #비용 수정
                distance[next] = cost
                #우선순위큐에 삽입
                heapq.heappush(hq,(cost,next))
    #distance배열 반환
    return distance

N = int(input())
graph = [[]for _ in range(N+1)]

for i in range(int(input())):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

S,D = map(int,input().split())

result = dijkstra(N,graph,S)
print(result[D])