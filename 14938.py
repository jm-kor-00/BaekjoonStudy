import sys
from collections import deque
import heapq
input =  sys.stdin.readline

N,M,R = map(int,input().split())
point = list(map(int,input().split()))
graph = [[float('inf')for _ in range(N)] for _ in range(N)]

for i in range(N):
    graph[i][i] = 0

for _ in range(R):
    s,e,w = map(int,input().split())
    graph[s-1][e-1] = w; graph[e-1][s-1] = w

for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            if graph[i][j] > graph[i][k] + graph[k][j] :
                graph[i][j] = graph[i][k] + graph[k][j]

score = [0] * N
for s in range(N):
    for e in range(N):
        if graph[s][e] <= M :
            score[s] += point[e]
            
print(max(score))