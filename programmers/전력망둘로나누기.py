from collections import deque

def BFS(graph,S):
    visited = {}; N = 0
    for key in graph.keys():
        visited[key] = False

    que = deque()
    que.append(S)
    visited[S] = True

    while que:
        t = que.popleft()
        N += 1
        if not t in graph.keys() : break
        for nxt in graph[t]:
            if visited[nxt]: continue
            que.append(nxt)
            visited[nxt] = True
    return N

def solution(n, wires):
    MIN = 101
    for i in range(n-1):
        graph = {}
        A, B = 0, 0
        for j in range(n-1):
            u = wires[j][0]; v = wires[j][1]
            if i == j:
                A,B = u, v
            else :
                if u in graph: 
                    graph[u].append(v)
                else : 
                    graph[u] = [v]
                if v in graph: 
                    graph[v].append(u)
                else :
                    graph[v] = [u]
        NA = BFS(graph,A)
        NB = BFS(graph,B)
        MIN = min(abs(NA - NB),MIN)
    return MIN