import sys
from collections import deque
input = sys.stdin.readline

#st에서 dt를 탐색할 수 있는지 => 인접여부 판단 함수
def isTouchable(st:list,dt:list):
    #[0],[1] : x,y / [2] : radius
    if (st[0] - dt[0])**2 + (st[1] - dt[1])**2 <= st[2]**2:
        return True
    else:
        return False
    
def bfs(G:list,V:int)->int:
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
            #인접리스트 형태로 그래프를 생성
            if isTouchable(st,dt):
                #i에서 j에 갈 수 있다면
                graph[i].append(j)

    MAX = 0
    for node in range(N):
       MAX = max(MAX, bfs(graph,node))
    
    print(MAX)