import sys
from collections import deque

queue = deque()
input = sys.stdin.readline

N = int(input())
V = int(input())
visited = [False] * N
count = 0
list = [[False for i in range(N)] for j in range(N)]

for i in range(V):
    A,B = map(int,input().split())
    list[A-1][B-1] = list[B-1][A-1] = True

queue.append(0)
while(queue):
    tmp = queue.popleft()
    visited[tmp] = True
    count += 1
    for i in range(N):
        if list[tmp][i] and not visited[i]:
            queue.append(i)
count = 0
for el in visited:
    if el : count += 1
print(count - 1)