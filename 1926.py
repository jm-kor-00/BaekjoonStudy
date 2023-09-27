import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

N,M = map(int,input().split())
G = []
visited = [[False for _ in range(M)] for _ in range(N)]

for _ in range(N):
    G.append(list(map(int,input().split())))

def BFS(graph,N ,M ,S):
    global visited
    queue = deque()
    queue.append(S)
    visited[S[0]][S[1]] = True
    cnt = 1

    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            tx,ty = x+dx[i], y+dy[i]
            
            if tx >= 0 and tx < N and ty >= 0 and ty < M:
                if not visited[tx][ty] and graph[tx][ty] == 1:
                    queue.append((tx,ty))
                    visited[tx][ty] = True
                    cnt += 1
    
    return cnt

max = 0
count = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and G[i][j] == 1: 
            tmp = BFS(G,N,M,(i,j))
            if tmp > max : max = tmp
            count += 1

print(count)
print(max)