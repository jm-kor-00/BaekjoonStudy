import sys
input = sys.stdin.readline

N, K = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
S, R, C = map(int,input().split())

virusArr = []
for i in range(N):
    for j in range(N):
        if board[i][j] > 0:
            virusArr.append((board[i][j],i,j))

dx = [-1,1,0,0];dy = [0,0,1,-1]
for _ in range(S):
    virusArr.sort(key= lambda x:x[0])
    VL = len(virusArr)
    for e in range(VL):
        v,x,y = virusArr[e]
        for i in range(4):
            tx,ty = x+dx[i],y+dy[i]
            if not 0 <= tx < N or not 0 <= ty < N : continue
            if board[tx][ty] != 0 : continue
            board[tx][ty] = v
            virusArr.append((v,tx,ty))
    virusArr = virusArr[VL:]
    
print(board[R-1][C-1])