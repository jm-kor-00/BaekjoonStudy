import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
N, V = map(int,input().split())
list = [[False for i in range(N + 1)] for j in range(N + 1)]
for _ in range(V): 
    A, B = map(int,input().split())
    list[A][B] = list[B][A] = True

Bacon = [0,0]
for i in range(1,N + 1):
    visited = [0] * (N + 1)
    queue.append(i)
    count = 0
    depth = 0
    while(queue):
        depth += 1
        for k in range(len(queue)):
            tmp = queue.popleft()
            for j in range(1,N+1):
                if list[tmp][j] and not visited[j]:
                    queue.append(j)
                    visited[j] = depth
    count = sum(visited)
    if Bacon[0] == 0:
        Bacon[0] = count
        Bacon[1] = i
    elif Bacon[0] > count:
        Bacon[0] = count
        Bacon[1] = i
print(Bacon[1])