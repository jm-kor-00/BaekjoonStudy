import sys
from collections import deque
input = sys.stdin.readline

def BFS(graph, NoLie, S):
    visited = [False for _ in range(len(graph))]
    que = deque()
    que.append(S-1)
    visited[S-1] = True
    while que :
        tmp = que.popleft()
        if tmp in NoLie : return False
        for nxt in range(len(graph[tmp])):
            if graph[tmp][nxt] == False :
                continue
            if visited[nxt] : continue
            que.append(nxt)
            visited[nxt] = True
    return True

N, M = map(int,input().split())
All = [True for _ in range(N)]
NoLie = list(map(int,input().split()))
if len(NoLie) == 1:
    NoLie = []
else :
    NoLie = NoLie[1:]
    for i in range(len(NoLie)):
        NoLie[i] -= 1

Parties = []
graph = [[False for _ in range(N)]for _ in range(N)]

for _ in range(M):
    party = list(map(int,input().split()))
    Parties.append(party[1:])
    for u in party[1:]:
        for v in party[1:]:
            graph[u-1][v-1] = True

res = 0
for party in Parties:
    if BFS(graph, NoLie, party[0]):
        res += 1
print(res)