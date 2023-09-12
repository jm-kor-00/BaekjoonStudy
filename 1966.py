import sys
from collections import deque
from heapq import heappush, heappop

input = sys.stdin.readline


def checking(queue, pQueue, target):
    count = 1
    while pQueue:
        Max = (-1) * heappop(pQueue)
        while queue:
            tmp = queue.popleft()
            if tmp[0] == Max:
                break
            else:
                queue.append(tmp)
        if tmp[1] == target:
            return count
        else:
            count += 1


for _ in range(int(input())):
    N, target = map(int, input().split())
    arr = list(map(int, input().split()))
    Queue = deque()
    pQueue = []
    for i in range(N):
        Queue.append([arr[i], i])
        heappush(pQueue, (-1) * arr[i])

    print(checking(Queue, pQueue, target))
