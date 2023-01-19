import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int,input().split())
graph = [[0 for i in range(N)] for i in range(N)]

visited_BFS = [False] * N
visited_DFS = [False] * N

def DFS(V):
    global visited_DFS
    visited_DFS[V] = True
    print(V + 1, end = ' ')
    for i in range(N):
        if graph[V][i] == 1 and not visited_DFS[i] :
            DFS(i)

def BFS(V):
    global visited_BFS
    que = deque()
    que.append(V)
    visited_BFS[V] = True
    while(que):
        tmp = que.popleft()
        print(tmp + 1,end = ' ')
        for i in range(N):
            if graph[tmp][i] == 1 and not visited_BFS[i] :
                que.append(i)
                visited_BFS[i] = 1
    visited_BFS = [False] * N

for i in range(M):
    S,E = map(int,input().split())
    graph[S - 1][E - 1] = 1
    graph[E - 1][S - 1] = 1

DFS(V - 1)
print()
BFS(V - 1)