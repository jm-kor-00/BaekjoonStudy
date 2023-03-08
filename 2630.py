import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input())

board = []
result = [0,0]

for i in range(N):
    row = list(map(int,input().split()))
    board.append(row)

def cutting(N,c,r):
    success = True
    init = board[r][c]
    for i in range(c,c + N):
        for j in range(r,r + N):
            if init != board[j][i]:
                success = False
    if success : result[init] += 1
    else :
        cutting(N // 2,c,r)
        cutting(N // 2,c + N // 2,r)
        cutting(N // 2,c,r + N // 2)
        cutting(N // 2,c + N // 2,r + N // 2)

cutting(N,0,0)
print(result[0]);print(result[1])