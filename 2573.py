import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

N,M = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

def BFS(board,N,M,S):
    global visited
    global melted
    queue = deque()
    queue.append(S)
    
    while queue:
        x,y = queue.popleft()
        near_0 = 0
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= N or ty < 0 or ty >= M:
                continue
            if board[tx][ty] < 1:
                near_0 += 1
            elif not visited[tx][ty]:
                visited[tx][ty] = True
                queue.append((tx,ty))
        melted[x][y] = board[x][y] - near_0

res = 1
year = 0
while res == 1:
    res = 0
    visited = [[False for _ in range(M)]for _ in range(N)]
    melted = [[0 for _ in range(M)]for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and not visited[i][j]:
                BFS(board,N,M,(i,j))
                res += 1
    year += 1
    board = melted
print(year - 1 if res > 1 else 0)