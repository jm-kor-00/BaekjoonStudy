import sys
input = sys.stdine.readline
R, C, T = map(int,input().split())

board = []
for _ in range(R):
    board.append(list(map(int,input().split())))

for i in range(R):
    if board[i][0] == -1:
        S = [i,i+1]; break

wind0 = []; wind1 = []
for c in range(1,C):
    wind0.append([S[0],c])
    wind1.append([S[1],c])
for r in range(S[0],-1,-1):
    wind0.append([r,C-1])
for r in range(S[1],C):
    wind1.append([r,C-1])
for c in range(C-1,-1,-1):
    wind0.append([0,c])
    wind1.append([R-1,c])
for r in range(S[0]):
    wind0.append([r,0])
for r in range(R-1,S[0],-1):
    wind1.append([r,0])

def circulate(R, C, S, T, board, wind0, wind1):
    change = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] > 0 : continue
            cnt = 0
            for i in range(4):
                tx,ty = r + dx[i], c + dy[i]
                if tx < 0 or tx >= len(board) or ty < 0 or ty >= len(board[0]):
                    continue
                if tx in S and ty == 0 : continue
                change[tx][ty] += board[r][c]//5
                cnt += 1
            change[r][c] -= cnt * (board//5)
    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] += change[r][c]

    for i in range(T):
        board[wind0[i][0]][wind0[i][1]] = 0
        board[wind1[i][0]][wind1[i][1]] = 0

    
    

          
    

                
                

    
