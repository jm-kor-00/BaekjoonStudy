from collections import deque
import sys
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]
N, M = map(int,input().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(int,input().split())))

init_safe = 0
virus_point = []
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0:
            init_safe += 1
        if MAP[i][j] == 2:
            virus_point.append((i,j))
init_safe -= 3 #벽세운개수
infected = init_safe
def bfs():
    global infected
    tmp_count = 0
    queue = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    for el in virus_point:
        queue.append(el)
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            tmp_x = x + dx[i]
            tmp_y = y + dy[i]
            if 0 <= tmp_x < N and 0 <= tmp_y < M:
                if MAP[tmp_x][tmp_y] == 0 and not visited[tmp_x][tmp_y]:
                    visited[tmp_x][tmp_y] = True
                    tmp_count += 1
                    queue.append((tmp_x,tmp_y))
    infected = min(infected,tmp_count)

def wall_making(count):
    if count == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 0:
                MAP[i][j] = 1
                wall_making(count + 1)
                MAP[i][j] = 0
wall_making(0)
print(init_safe - infected)