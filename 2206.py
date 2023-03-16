import sys
from collections import deque as dq
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]
queue = dq()
queue.append((0,0,0))
board = []

N, M = map(int,input().split())
for _ in range(N):
    board.append(list(input().strip()))

visited = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]

result = -2
while(queue):
    x,y,w = queue.popleft()
    if x == N-1 and y == M-1 :
        result = visited[x][y][w];break
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if not ((0 <= tx < N) and (0 <= ty < M)):
            continue
        if board[tx][ty] == '1' and w == 0 :
            visited[tx][ty][1] = visited[x][y][0] + 1
            queue.append((tx,ty,1))
            continue
        elif board[tx][ty] == '0' and visited[tx][ty][w] == 0 :
            visited[tx][ty][w] = visited[x][y][w] + 1
            queue.append((tx,ty,w))
print(result + 1)