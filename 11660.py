import sys
input = sys.stdin.readline

N,M = map(int,input().split())
board = [[0 for _ in range(N+1)]for _ in range(N+1)]
for i in range(1,N+1):
    row = list(map(int,input().split()))
    for j in range(1,N+1):
        board[i][j] = row[j-1]

for i in range(1,N+1):
    for j in range(1,N+1):
        board[i][j] += board[i][j-1]
for i in range(1,N+1):
    for k in range(1,N+1):
        board[k][i] += board[k-1][i]
        
for _ in range(M):
    a, b, c, d = map(int,input().split())
    print(board[c][d] - board[c][b-1] - board[a-1][d] + board[a-1][b-1])