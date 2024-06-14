import sys
from collections import deque
input = sys.stdin.readline

#bfs 로 섬 만들고 걔네들끼리 평균치 내리기
#섬이 만들어지면 moved = True
# while moved == False
    
def BFS(visited,Board,S):
    que = deque()
    que.append(S)
    while que :
        x,y = que.popleft()
        for i in range(4):
            que.append((r,c))
                while que :
                    x,y = que.popleft()
                    for i in range(4):
                        tx,ty = x + dx[i], y + dy[i]

def solution():
    N, L, R = map(int,input().split())
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    Board = []
    for _ in range(N):
        Board.append(list(map(int, input().split())))

    moved = False
    while moved == False:
        visited = [[False for _ in range(N)] for _ in range(N)]
        que = deque()
        for r in range(N):
            for c in range(N):
                if visited[r][c] :
                    continue
                        