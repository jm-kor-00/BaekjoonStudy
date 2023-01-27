import sys
from collections import deque
input = sys.stdin.readline

def CicleCountBFS(N,graph):
    queue = deque()
    Circle_count = 0
    visited = [False] * (N + 1)
    for i in range(1,N + 1):
        if visited[i] : continue
        queue.append(i)
        while(queue):
            tmp = queue.popleft()
            visited[tmp] = True
            if not visited[graph[tmp - 1]]:
                queue.append(graph[tmp - 1])
        Circle_count += 1
    return Circle_count

T = int(input())
for _ in range(T):
    N = int(input())
    graph = list(map(int,input().split()))
    print(CicleCountBFS(N,graph))