from collections import deque
import sys
input = sys.stdin.readline

R,C = map(int,input().split())
board = [[-1 for _ in range(C+2)]for _ in range(R+2)]
for i in range(R):
    tmp = list(map(int,input().split()))
    for j in range(C):
        board[i+1][j+1] = tmp[j]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def BFS(r,c):
    global board,R,C
    que = deque()
    visited = set([])
    que.append((r,c))
    visited.add((r,c))
    isOut = False
    while que :
        tr,tc = que.popleft()
        for i in range(4):
            nr,nc = tr+dx[i], tc+dy[i]
            if (nr,nc) in visited : continue
            if board[nr][nc] == -1 : isOut = True;continue
            elif board[nr][nc] == 0 :
                que.append((nr,nc))
                visited.add((nr,nc))
    if isOut :
        for x,y in visited:
            board[x][y] = -1

def check_area():
    global R,C,board
    for i in range(1,R+1):
        for j in range(1,C+1):
            if board[i][j] != 0 : continue
            BFS(i,j)

def check_cheese():
    global R,C,board
    for i in range(1,R+1):
        for j in range(1,C+1):
            if board[i][j] == 1:
                return True
    return False

def del_cheese():
    global R,C,board
    change = []
    for i in range(1,R+1):
        for j in range(1,C+1):
            if board[i][j] != 1 : continue
            cnt = 0
            for k in range(4):
                ti,tj = i+dx[k], j+dy[k]
                if board[ti][tj] == -1 : cnt += 1
            if cnt >= 2 : change.append((i,j))
    for x,y in change:
        board[x][y] = -1

ans = 0
while True:
    check_area()
    if not check_cheese():break
    del_cheese()
    ans += 1

print(ans)