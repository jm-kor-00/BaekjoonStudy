import sys
from collections import deque
input = sys.stdin.readline

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.edges = []  # List to store all edges
        self.edges_sorted = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))
        self.edges_sorted[u].append((v,weight))

    def bfs(self,src,dest):
        visited = [False for _ in range(self.V)]
        que = deque()
        que.append(src)
        visited[src] = True
        while que:
            tmp = que.popleft()
            if tmp == dest : return True
            for v,w in self.edges_sorted[src]:
                if not visited[v]:
                    que.append(v)
                    visited[v] = True
        return False

    def bellman_ford(self, src):
        # Step 1: Initialize distances from src to all other vertices as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times.
        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: Check for negative-weight cycles.
        for u, v, w in self.edges:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                if self.bfs(v,src) : return True
        return False

    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

res = ["NO" for _ in range(int(input()))]

for tc in range(len(res)):
    N,M,W = map(int,input().split())
    graph = Graph(N)
    for _ in range(M):
        S, E, T = map(int,input().split())
        graph.add_edge(S-1,E-1,T)
        graph.add_edge(E-1,S-1,T)
    for _ in range(W):
        S, E, T = map(int,input().split())
        graph.add_edge(S-1,E-1,-T)
    dist = [False] * N
    for i in range(N):
        if dist[i] : 
        Bool, dist = graph.bellman_ford(i)
        if not Bool : continue
        for j in range(len(dist)):
        

for el in res:
    print(el)