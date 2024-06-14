from collections import deque
visited = []; N = 0

def BFS(graph,S):
    global visited, N
    que = deque(); que.append(S)
    visited[S] = True
    while que:
        t = que.popleft()
        for i in range(N):
            if t == i : continue
            elif graph[t][i] == 0 : continue
            if not visited[i]:
                visited[i] = True
                que.append(i)

def solution(n, computers):
    global visited, N
    visited = [False for _ in range(n)]
    N = n
    
    res = 0
    for node in range(n):
        if not visited[node]:
            BFS(computers, node)
            res += 1
            
    return res