import sys
from collections import deque

input = sys.stdin.readline

N,Q = map(int,input().split())
USADO = [[]for _ in range(N+1)]
for _ in range(N-1):
    s,e,w = map(int,input().split())
    USADO[s].append((e,w))
    USADO[e].append((s,w))

def BFS(N,K,V):
    queue = deque()
    visited = [False] * (N+1)
    
    visited[V] = True
    queue.append((V,float('inf')))
    cnt = 0

    while queue :
        tmp,w = queue.popleft()
        for nxt,nw in USADO[tmp]:
            newU = min(w,nw)
            if not visited[nxt]:
                queue.append((nxt,newU))
                visited[nxt] = True
                if newU >= K :
                    cnt += 1
                    # print(nxt,newU)
    return cnt

for _ in range(Q):
    K,V = map(int,input().split())
    print(BFS(N,K,V))