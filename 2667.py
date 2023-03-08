from collections import deque

N = int(input())
graph = []
result = []

for _ in range(N):
    graph.append(list(map(int,input().strip())))

def BFS(graph,N,i,j):
    queue = deque()
    queue.append((i,j))
    graph[i][j] = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    count = 1
    while(queue):
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx,ny))
                    count += 1
    return count

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(BFS(graph,N,i,j))
result.sort()
print(len(result))
for el in result:
    print(el)