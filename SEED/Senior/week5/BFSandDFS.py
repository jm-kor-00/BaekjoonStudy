from collections import deque

def BFS(graph,V):
    N = len(graph)
    visited = [False] * N
    visited[V] = True
    que = deque()
    que.append(V)
    while(que):
        tmp = que.popleft()
        for i in range(N):
            if graph[tmp][i] == 1 and not visited[i] :
                que.append(i)
                visited[i] = True

def DFS(graph, V):
    N = len(graph)
    visited = [False] * N
    visited[V] = True
    stack = deque()
    stack.append(V)
    while(stack):
        tmp = stack.pop()
        for i in range(N-1,-1,-1):
            if graph[tmp][i] == 1 and not visited[i] :
                stack.append(i)
                visited[i] = True

from itertools import permutations

import bisect

arr = [1,2,3,4,5]
print(bisect.bisect_left(arr,3))
print(bisect.bisect_right(arr,3))