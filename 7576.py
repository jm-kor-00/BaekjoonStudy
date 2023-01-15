import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
board = []
queue = deque()
result = 0

for i in range(K):
    board.append(list(map(int,input().split())))

for i in range(N):
    for j in range(K):
        if board[j][i] == 1:
            queue.appendleft((i,j))
while(queue):
    for t in range(len(queue)):
        x,y = queue.pop()
        if x + 1 < N :
            if board[y][x+1] == 0 : 
                board[y][x+1] = 1
                queue.appendleft((x+1,y))
        if x - 1 >= 0 :
            if board[y][x-1] == 0 : 
                board[y][x-1] = 1
                queue.appendleft((x-1,y))
        if y + 1 < K :
            if board[y+1][x] == 0 : 
                board[y + 1][x] = 1
                queue.appendleft((x,y+1))
        if y - 1 >= 0 :
            if board[y - 1][x] == 0 : 
                board[y - 1][x] = 1
                queue.appendleft((x,y-1))
    if len(queue) == 0 :
        break
    else : result += 1

for i in range(N):
    for j in range(K):
        if board[j][i] == 0 : 
            result = -1
            break
print(result)