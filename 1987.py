import sys
input = sys.stdin.readline

R, C = map(int,input().split())
board = []
for _ in range(R):
    board.append(list(input().strip()))

dx = [0,0,-1,1];dy = [1,-1,0,0]
max_depth = 1
visited = [False for _ in range(26)]

def DFS(r,c,depth):
    global max_depth
    max_depth = max(max_depth,depth)
    for i in range(4):
        tr,tc = r+dx[i], c+dy[i]
        if 0 <= tr < len(board) and 0 <= tc < len(board[0]):
            if not visited[ord(board[tr][tc])-65]:
                visited[ord(board[tr][tc])-65] = True
                DFS(tr,tc,depth+1)
                visited[ord(board[tr][tc])-65] = False

visited[ord(board[0][0])-65] = True
DFS(0,0,1)
print(max_depth)