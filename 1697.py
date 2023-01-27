import sys
from collections import deque
input = sys.stdin.readline

MAX = 100000
queue = deque()

N, M = map(int,input().split())
visited = [False] * (MAX + 1)
visited[N] = 0

queue.append(N)
while(queue):
    tmp = queue.popleft()
    if tmp == M : break
    for next in (tmp-1, tmp+1, tmp * 2):
        if 0 <= next <= MAX and not visited[next]:
            queue.append(next)
            visited[next] = visited[tmp] + 1
print(visited[M])