import sys
from collections import deque
input = sys.stdin.readline

def isTouchable(st,dt):
    if (st[0] - dt[0])**2 + (st[1] - dt[1])**2 <= st[2]**2:
        return True
    else:
        return False
    
def bfs(G,V):
    visit = [False] * len(G)
    que = deque()
    que.append(V)
    visit[V] = True
    cnt = 1

    while que:
        tmp = que.popleft()
        for nxt in G[tmp]:
            if not visit[nxt]:
                que.append(nxt)
                visit[nxt] = True
                cnt += 1

    return cnt
    
for _ in range(int(input())):
    galaxy = []
    N = int(input())
    for _ in range(N):
        galaxy.append(list(map(int,input().split())))

    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j : continue
            st = galaxy[i]
            dt = galaxy[j]
            if isTouchable(st,dt):
                graph[i].append(j)
    MAX = 0
    for node in range(N):
       MAX = max(MAX, bfs(graph,node))
    
    print(MAX)