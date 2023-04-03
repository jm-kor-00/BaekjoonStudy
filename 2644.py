import sys
from collections import deque
input = sys.stdin.readline

def BFS(N,graph,S,E):
    queue = deque()
    queue.append(S)
    count = 0
    visited = [0] * (N+1)
    while queue:
        count += 1
        for _ in range(len(queue)):
            tmp = queue.popleft()
            for nxt in graph[tmp]:
                if not visited[nxt]:
                    queue.append(nxt)
                    visited[nxt] = count
    if visited[E] != 0 : return visited[E]
    else : return -1

N = int(input())
S,E = map(int,input().split())
graph = [[]for _ in range(N+1)]

for _ in range(int(input())):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(BFS(N,graph,S,E))