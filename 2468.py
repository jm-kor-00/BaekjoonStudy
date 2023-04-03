import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

MAX = 0
for i in range(N):
    for j in range(N):
        if board[i][j] > MAX :
            MAX = board[i][j]

def BFS(N,sink,S):
    global visited
    queue = deque()
    queue.append(S)
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= N or ty < 0 or ty >= N:
                continue
            if not visited[tx][ty] and board[tx][ty] > sink:
                queue.append((tx,ty))
                visited[tx][ty] = True

count = [0] * (MAX + 2)
for sink in range(MAX,-1,-1):
    visited = [[False for _ in range(N)]for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] > sink:
                count[sink] += 1
                BFS(N,sink,(i,j))

print(max(count))