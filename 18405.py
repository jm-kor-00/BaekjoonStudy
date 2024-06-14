import sys
input = sys.stdin.readline

def available_pos(board,x,y):
    arr = []
    dx = [-1,1,0,0];dy = [0,0,1,-1]
    for i in range(4):
        tx = x+dx[i]; ty = y+dy[i]
        if 0 <= tx < len(board) and 0 <= ty < len(board[0]):
            if board[tx][ty] > 0 : arr.append(board[tx][ty])
    if len(arr) == 0 : return 0
    return min(arr)

N, K = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
S, R, C = map(int,input().split())
dx = [-1,1,0,0];dy = [0,0,1,-1]

while S > 0:
    arr = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 : continue
            for x in range(4):
                tx = i+dx[x]; ty = j+dy[x]
                if 0 <= tx < len(board) and 0 <= ty < len(board[0]):
            if board[tx][ty] > 0 : arr.append(board[tx][ty])

print(board[R-1][C-1])