import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

for i in range(N):
    queue.append(i)
    visited = [0] * N
    while(queue):
        tmp = queue.popleft()
        for j in range(N):
            if graph[tmp][j] == 1 and visited[j] != 1:
                queue.append(j)
                visited[j] = 1
    for el in visited:
        print(el,end=' ')
    print()