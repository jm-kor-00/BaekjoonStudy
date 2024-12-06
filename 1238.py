import sys
from collections import deque
import heapq
input = sys.stdin.readline

N,M,X = map(int,input().split()); X -= 1
graph = [[]for _ in range(N)]
for _ in range(M):
    s,e,w = map(int,input().split())
    graph[s-1].append((e-1,w))

def dijkstra(start):
    global graph,N
    q = []
    heapq.heappush(q, (0, start)) # 우선순위, 값 형태로 들어간다.
    distance = [float('inf')] * N
    distance[start] = 0 
    while q:
        dist, now = heapq.heappop(q) # 우선순위가 가장 낮은 값(가장 작은 거리)이 나온다.
        if distance[now] < dist: # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
            continue               # 따라서 다음으로 넘어간다.
        for i in graph[now]:     # 연결된 모든 노드 탐색
            if dist+i[1] < distance[i[0]]: # 기존에 입력되어있는 값보다 크다면
                distance[i[0]] = dist+i[1]   #
                heapq.heappush(q, (dist+i[1], i[0]))
    return distance

#distance[x][y] = x에서 y로 가는 최소 가중치

#n -> goal
distance = [0] * N
for i in range(N):
    tmp = dijkstra(i)
    if i == X :
        comeback = tmp
    distance[i] += tmp[X]

for i in range(N):
    distance[i] += comeback[i]

print(max(distance))