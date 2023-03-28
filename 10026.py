import sys
from copy import deepcopy as dcp
from collections import deque
input = sys.stdin.readline

#BFS 돌때 필요한 4가지 방향을 미리 배열로 선언
dx = [1,-1,0,0]
dy = [0,0,1,-1]

#너비우선탐색 (시작점과 같은 색만 탐색)
#두 보드의 visited배열이 다르므로, visited배열도 인자로 받음
def BFS(board,start,visited):
    queue = deque()
    queue.append(start)
    #시작점 색깔 저장
    color = board[start[0]][start[1]]
    while(queue):
        x,y = queue.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            #보드 밖으로 나가지 않게 인덱스 제어
            if tx < 0 or tx >= N or ty < 0 or ty >= N:
                continue
            #방문전 + 색깔 같은 노드만 탐색
            if not visited[tx][ty] and board[tx][ty] == color:
                #큐에 삽입, 방문처리
                queue.append((tx,ty))
                visited[tx][ty] = True

#보드의 크기와 보드 입력 받음
board = []
N = int(input())
for _ in range(N):
    board.append(list(input().strip()))
#abnormal(색약) 탐색에 사용할 보드를 deepcopy로 생성
board_abn = dcp(board)
#색약은 'R'과 'G'를 구별하지 못하므로 모든 R을 G로 변경
for i in range(N):
    for j in range(N):
        if board_abn[i][j] == 'R':
            board_abn[i][j] = 'G'

# print(board)
# print(board_abn)

#탐색시 방문,미방분 노드 구별을 위해 visited배열을 만들어서 사용
visited = [[False for _ in range(N)] for _ in range(N)]
visited_abn = [[False for _ in range(N)] for _ in range(N)]
#각각의 구별되는 개수를 나타낼 변수
normal = 0
abnormal = 0

#BFS를 사용하여 구역 개수를 찾음
for i in range(N):
    for j in range(N):
        if not visited[i][j] :
            normal += 1
            BFS(board,(i,j),visited) 

for i in range(N):
    for j in range(N):
        if not visited_abn[i][j] :
            abnormal += 1
            BFS(board_abn,(i,j),visited_abn)

#결과출력
print(normal,abnormal)