from collections import deque
from itertools import combinations
from copy import deepcopy
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
lab = []

N, M = map(int,input().split())
for _ in range(N):
    lab.append(list(map(int,input().split())))

MIN = float('inf')
virus = []

for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append((i,j))

def BFS(N,initial,graph):
    global MIN
    visited = [[False for _ in range(N)] for _ in range(N)]
    hour = 0

    queue = deque()
    for el in initial:
        visited[el[0]][el[1]] = True
        queue.append(el)

    tmp_left = len(queue)
    while queue :
        if tmp_left == 0:
            hour += 1
            tmp_left = len(queue)

        tmp_left -= 1
        x, y = queue.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or tx >= N or ty < 0 or ty >= N : continue
            if graph[tx][ty] == 1:
                continue
            elif not visited[tx][ty] :
                if graph[tx][ty] == 2:
                    tmp_left += 1
                    queue.appendleft((tx,ty))
                else :
                    queue.append((tx,ty))
                visited[tx][ty] = True

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] != 1 : return False

    if hour < MIN :
        MIN = hour
        return True

for initial in combinations(virus,M):
    BFS(N,initial,lab)

if MIN == float('inf'):
    print(-1)
else : print(MIN)