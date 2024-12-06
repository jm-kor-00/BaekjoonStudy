import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[]for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(S,N):
    visited = [0 for _ in range(N+1)]
    que = deque()
    que.append(1)
    visited[1] = 1
    while que:
        t = que.popleft()
        for c in graph[t]:
            if visited[c] != 0 : continue
            que.append(c)
            visited[c] = t
    return visited

ANS = bfs(1,N)
for el in ANS[2:]:
    print(el)