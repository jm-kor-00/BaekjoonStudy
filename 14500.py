import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

visited = [[False for _ in range(M)]for _ in range(N)]
dx = [0,0,1,-1]; dy = [1,-1,0,0]
MAX = 0; tmp = 0

def tetromino(x,y,cnt):
    global MAX,tmp, M, N
    if cnt == 4:
        if tmp > MAX : 
            MAX = tmp
        return
    
    for i in range(4):
        tx,ty = x+dx[i], y+dy[i]
        if 0 <= tx < N and 0 <= ty < M:
            if visited[tx][ty] : continue
            
            tmp += board[tx][ty]
            visited[tx][ty] = True
            tetromino(tx,ty,cnt+1)
            tmp -= board[tx][ty]
            visited[tx][ty] = False

def spc(r,c):
    sum = 0
    dr = [0,-1,-1,-1]
    dc = [0,-1,0,1]
    if c == 0 or c == M-1 : return
    if r > 0 and c > 0:
        for i in range(4):
            tr,tc = r+dr, c+dc
            sum += board[tr][tc]
    
    for i in range(4):
        tr,tc = r+dr, c+dc
        if 0 <= tr < N and 0 <= tc < M:
            sum += board[tr][tc]
        else : return

for i in range(N):
    for j in range(M):
        tetromino(i,j,0)   
print(MAX)