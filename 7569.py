import sys
from collections import deque
input = sys.stdin.readline

N,K,H = map(int,input().split())
board = []
queue = deque()
result = 0

board = [] 

for i in range(H):
    board.append([])
    for k in range(K):
        board[i].append(list(map(int,input().split())))

# for i in range(H):
#     for k in range(K):
#         for j in range(N):
#             print(board[i][k][j],end = ' ')
#         print()
#     print()

for i in range(N):
    for j in range(K):
        for k in range(H):
            if board[k][j][i] == 1:
                queue.appendleft((i,j,k))
                
while(queue):
    for t in range(len(queue)):
        x,y,z = queue.pop()
        # print(x,y,z)
        if x + 1 < N :
            if board[z][y][x+1] == 0 : 
                board[z][y][x+1] = 1
                queue.appendleft((x+1,y,z))
        if x - 1 >= 0 :
            if board[z][y][x-1] == 0 : 
                board[z][y][x-1] = 1
                queue.appendleft((x-1,y,z))
        if y + 1 < K :
            if board[z][y+1][x] == 0 : 
                board[z][y + 1][x] = 1
                queue.appendleft((x,y+1,z))
        if y - 1 >= 0 :
            if board[z][y - 1][x] == 0 : 
                board[z][y - 1][x] = 1
                queue.appendleft((x,y-1,z))
        if z + 1 < H :
            if board[z+1][y][x] == 0 : 
                board[z+1][y][x] = 1
                queue.appendleft((x,y,z+1))
        if z - 1 >= 0 :
            if board[z-1][y][x] == 0 : 
                board[z-1][y][x] = 1
                queue.appendleft((x,y,z-1))
    if len(queue) == 0 :
        break
    else : result += 1

for i in range(N):
    for j in range(K):
        for k in range(H):
            if board[k][j][i] == 0 : 
                result = -1
                break
print(result)