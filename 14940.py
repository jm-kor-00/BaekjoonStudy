import sys
from collections import deque

def BFS(board,sx,sy):
    visited = [[0 for _ in range(len(board[0]))]for _ in range(len(board))]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    que = deque()
    que.append((sx,sy,0))
    visited[sx][sy] = 1
    while que:
        tx,ty,tD = que.popleft()
        tD += 1
        for dir in range(4):
            nx,ny = tx + dx[dir], ty + dy[dir]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                if board[nx][ny] == 0 or visited[nx][ny] != 0 : continue
                visited[nx][ny] = tD
                que.append((nx,ny,tD))
    for r in range(len(board)):
        for c in range(len(board[0])):
            if visited[r][c] == 0:
                if board[r][c] != 0:
                    visited[r][c] = -1
    visited[sx][sy] = 0
    return visited

def solution():
    input = sys.stdin.readline
    N, M = map(int,input().split())
    Board = []
    for _ in range(N):
        Board.append(list(map(int,input().split())))
    
    for r in range(N):
        for c in range(M):
            if Board[r][c] == 2:
                sx,sy = r,c
                res = BFS(Board,sx,sy)
                for row in res:
                    for ch in row:
                        print(ch,end=' ')
                    print()
                return
                
solution()