import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[False for i in range(N)] for i in range(N)]
visited = [False] * N

def BFS(V):
    que = deque()
    que.append(V)
    visited[V] = True
    while(que):
        tmp = que.popleft()
        # print(tmp + 1,end = ' ')
        for i in range(N):
            if graph[tmp][i] and not visited[i] :
                que.append(i)
                visited[i] = 1

for i in range(M):
    u,v = map(int,input().split())
    graph[u - 1][v - 1] = True
    graph[v - 1][u - 1] = True

count = 0

for i in range(N):
    if not visited[i] :
        count += 1
        BFS(i)
print(count)